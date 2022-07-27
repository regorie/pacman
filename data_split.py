def create_lda_partitions(
    dataset: XY,
    dirichlet_dist: Optional[np.ndarray] = None,
    num_partitions: int = 100,
    concentration: Union[float, np.ndarray, List[float]] = 0.5,
    accept_imbalanced: bool = False,
    seed: Optional[Union[int, SeedSequence, BitGenerator, Generator]] = None,
) -> Tuple[XYList, np.ndarray]:
    """Create imbalanced non-iid partitions using Latent Dirichlet Allocation
    (LDA) without resampling.

    Args:
        dataset (XY): Dataset containing samples X and labels Y.
        dirichlet_dist (numpy.ndarray, optional): previously generated distribution to
            be used. This is useful when applying the same distribution for train and
            validation sets.
        num_partitions (int, optional): Number of partitions to be created.
            Defaults to 100.
        concentration (float, np.ndarray, List[float]): Dirichlet Concentration
            (:math:`\\alpha`) parameter. Set to float('inf') to get uniform partitions.
            An :math:`\\alpha \\to \\Inf` generates uniform distributions over classes.
            An :math:`\\alpha \\to 0.0` generates one class per client. Defaults to 0.5.
        accept_imbalanced (bool): Whether or not to accept imbalanced output classes.
            Default False.
        seed (None, int, SeedSequence, BitGenerator, Generator):
            A seed to initialize the BitGenerator for generating the Dirichlet
            distribution. This is defined in Numpy's official documentation as follows:
            If None, then fresh, unpredictable entropy will be pulled from the OS.
            One may also pass in a SeedSequence instance.
            Additionally, when passed a BitGenerator, it will be wrapped by Generator.
            If passed a Generator, it will be returned unaltered.
            See official Numpy Documentation for further details.

    Returns:
        Tuple[XYList, numpy.ndarray]: List of XYList containing partitions
            for each dataset and the dirichlet probability density functions.
    """
    # pylint: disable=too-many-arguments,too-many-locals

    x, y = dataset
    x, y = shuffle(x, y)
    x, y = sort_by_label(x, y)

    if (x.shape[0] % num_partitions) and (not accept_imbalanced):
        raise ValueError(
            """Total number of samples must be a multiple of `num_partitions`.
               If imbalanced classes are allowed, set
               `accept_imbalanced=True`."""
        )

    num_samples = num_partitions * [0]
    for j in range(x.shape[0]):
        num_samples[j % num_partitions] += 1

    # Get number of classes and verify if they matching with
    classes, start_indices = np.unique(y, return_index=True)

    # Make sure that concentration is np.array and
    # check if concentration is appropriate
    concentration = np.asarray(concentration)

    # Check if concentration is Inf, if so create uniform partitions
    partitions: List[XY] = [(_, _) for _ in range(num_partitions)]
    if float("inf") in concentration:

        partitions = create_partitions(
            unpartitioned_dataset=(x, y),
            iid_fraction=1.0,
            num_partitions=num_partitions,
        )
        dirichlet_dist = get_partitions_distributions(partitions)[0]

        return partitions, dirichlet_dist

   if concentration.size == 1:
        concentration = np.repeat(concentration, classes.size)
    elif concentration.size != classes.size:  # Sequence
        raise ValueError(
            f"The size of the provided concentration ({concentration.size}) ",
            f"must be either 1 or equal number of classes {classes.size})",
        )

    # Split into list of list of samples per class
    list_samples_per_class: List[List[np.ndarray]] = split_array_at_indices(
        x, start_indices
    )

    if dirichlet_dist is None:
        dirichlet_dist = np.random.default_rng(seed).dirichlet(
            alpha=concentration, size=num_partitions
        )

    if dirichlet_dist.size != 0:
        if dirichlet_dist.shape != (num_partitions, classes.size):
            raise ValueError(
                f"""The shape of the provided dirichlet distribution
                 ({dirichlet_dist.shape}) must match the provided number
                  of partitions and classes ({num_partitions},{classes.size})"""
            )

    # Assuming balanced distribution
    empty_classes = classes.size * [False]
    for partition_id in range(num_partitions):
        partitions[partition_id], empty_classes = sample_without_replacement(
            distribution=dirichlet_dist[partition_id].copy(),
            list_samples=list_samples_per_class,
            num_samples=num_samples[partition_id],
            empty_classes=empty_classes,
        )

    return partitions, dirichlet_dist
