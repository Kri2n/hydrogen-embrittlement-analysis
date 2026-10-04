from src.generate_data import make_dataset


def test_dataset_is_reproducible():
    assert make_dataset().equals(make_dataset())


def test_ductility_is_never_negative():
    assert (make_dataset()["RA_percent"] >= 0).all()


def test_ductility_decreases_with_hydrogen():
    df = make_dataset()
    means = df.groupby("H_conc_ppm")["RA_percent"].mean()
    assert means.loc[0] > means.loc[10]