import numpy as np
import h5py


f = h5py.File("db.hdf5", "a")

data_table_by_country = [
    dict(
        group="Country",
        values=np.array([
            np.string_("Income(USD)"),
            np.string_("Population Density(1000/km3)"),
            np.string_("Grown in Past 25 years (%) - 0"),
            np.string_("Grown in Past 25 years (%) - 10"),
            np.string_("Grown in Past 25 years (%) - 15"),
            np.string_("Grown in Past 25 years (%) - 25"),
        ]),
        dtype=h5py.string_dtype(encoding='utf-8')
    ),
    dict(group="Nepal", values=np.array([1500, 487.296, 5.4, 12.3, 25.3, 27.3]), dtype="f"),
    dict(group="India", values=np.array([1500, 487.296, 5.4, 12.3, 25.3, 27.3]), dtype="f"),
    dict(group="China", values=np.array([1500, 487.296, 5.4, 12.3, 25.3, 27.3]), dtype="f"),
    dict(group="Bangladesh", values=np.array([1500, 487.296, 5.4, 12.3, 25.3, 27.3]), dtype="f"),
    dict(group="USA", values=np.array([1500, 487.296, 5.4, 12.3, 25.3, 27.3]), dtype="f"),
]

group_by_country = f.create_group("GroupByCountry")
for data in data_table_by_country:
    result = group_by_country.create_dataset(data.get("group"), data=data.get("values"), dtype=data.get("dtype"))

group_by_age = f.create_group("/GroupByAge")

data_table_by_age = [
    dict(
        country="Column_Name",
        data_by_year=[
            dict(
                year="Column_Name",
                data=np.array([
                    [
                        np.string_("Age"),
                        np.string_("Income(USD)"),
                        np.string_("Express(USD)"),
                        np.string_("Crime(per 1000)"),
                        np.string_("Computers(per 1000)"),
                    ],
                ]),
                dtype=h5py.string_dtype(encoding='utf-8')
            )
        ]
    ),
    dict(
        country="India",
        data_by_year=[
            dict(
                year="2025",
                data=np.array([
                    [25, 2500, 7850, 0.078, 300],
                    [30, 2700, 1348, 0.097, 325],
                    [40, 5000, 2256, 0.115, 123],
                    [50, 2300, 5840, 0.129, 128],
                    [60, 2800, 1092, 0.138, 129],
                    [70, 2932, 2350, 0.138, 135],
                    [80, 2552, 3264, 0.138, 124]
                ]),
                dtype='f'
            ),
            dict(
                year="2250",
                data=np.array([
                    [25, 0, 7850, 0.95, 300],
                    [30, 200, 1348, 0.78, 325],
                    [40, 400, 2256, 0.115, 123],
                    [50, 600, 5840, 0.23, 128],
                    [60, 800, 1092, 0.138, 129],
                    [70, 1000, 2400, 0.75, 135],
                    [80, 2450, 1800, 0.138, 124]
                ]),
                dtype='f'
            )
        ]
    ),
]
for data in data_table_by_age:
    group_by_age_country = f.create_group("/GroupByAge/%s" % data.get("country"))
    for data_year in data.get("data_by_year"):
        result = group_by_age_country.create_dataset(
            "/GroupByAge/%s/%s" % (data.get("country"), data_year.get("year")),
            data=data_year.get("data"), dtype=data_year.get("dtype")
        )
