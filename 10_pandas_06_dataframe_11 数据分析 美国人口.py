from pandas import DataFrame


def create_state_abbrevs():
    """创建美国50个州的名称和缩写"""
    rows = [
        ['Alabama', 'AL'], ['Alaska', 'AK'], ['Arizona', 'AZ'], ['Arkansas', 'AR'],
        ['California', 'CA'], ['Colorado', 'CO'], ['Connecticut', 'CT'], ['Delaware', 'DE'],
        ['Florida', 'FL'], ['Georgia', 'GA'], ['Hawaii', 'HI'], ['Idaho', 'ID'],
        ['Illinois', 'IL'], ['Indiana', 'IN'], ['Iowa', 'IA'], ['Kansas', 'KS'],
        ['Kentucky', 'KY'], ['Louisiana', 'LA'], ['Maine', 'ME'], ['Maryland', 'MD'],
        ['Massachusetts', 'MA'], ['Michigan', 'MI'], ['Minnesota', 'MN'], ['Mississippi', 'MS'],
        ['Missouri', 'MO'], ['Montana', 'MT'], ['Nebraska', 'NE'], ['Nevada', 'NV'],
        ['New Hampshire', 'NH'], ['New Jersey', 'NJ'], ['New Mexico', 'NM'], ['New York', 'NY'],
        ['North Carolina', 'NC'], ['North Dakota', 'ND'], ['Ohio', 'OH'], ['Oklahoma', 'OK'],
        ['Oregon', 'OR'], ['Pennsylvania', 'PA'], ['Rhode Island', 'RI'], ['South Carolina', 'SC'],
        ['South Dakota', 'SD'], ['Tennessee', 'TN'], ['Texas', 'TX'], ['Utah', 'UT'],
        ['Vermont', 'VT'], ['Virginia', 'VA'], ['Washington', 'WA'], ['West Virginia', 'WV'],
        ['Wisconsin', 'WI'], ['Wyoming', 'WY']
    ]
    cols = ["State", "Abbreviation"]
    df_state_abbrevs = DataFrame(rows, columns=cols)
    print(df_state_abbrevs)
    print(df_state_abbrevs.shape)
    return df_state_abbrevs


def create_state_area():
    """创建美国50个州的名称和面积"""
    rows = [
        ['Alabama', 50709], ['Alaska', 1723337], ['Arizona', 1138257], ['Arkansas', 519592],
        ['California', 1559361], ['Colorado', 1038208], ['Connecticut', 591143], ['Delaware', 100417],
        ['Florida', 1931756], ['Georgia', 1021768], ['Hawaii', 270594], ['Idaho', 423159],
        ['Illinois', 1499950], ['Indiana', 705749], ['Iowa', 309041], ['Kansas', 288590],
        ['Kentucky', 639201], ['Louisiana', 464879], ['Maine', 132910], ['Maryland', 590632],
        ['Massachusetts', 689250], ['Michigan', 998685], ['Minnesota', 542038], ['Mississippi', 297614],
        ['Missouri', 604568], ['Montana', 99539], ['Nebraska', 182634], ['Nevada', 270055],
        ['New Hampshire', 132070], ['New Jersey', 888219], ['New Mexico', 208520], ['New York', 1957026],
        ['North Carolina', 1048808], ['North Dakota', 762062], ['Ohio', 1161342], ['Oklahoma', 395697],
        ['Oregon', 4217737], ['Pennsylvania', 1280250], ['Rhode Island', 105936], ['South Carolina', 514871],
        ['South Dakota', 884659], ['Tennessee', 645928], ['Texas', 2903760], ['Utah', 299591],
        ['Vermont', 62398], ['Virginia', 853551], ['Washington', 761489], ['West Virginia', 179214],
        ['Wisconsin', 582243], ['Wyoming', 578759]
    ]
    cols = ["State", "Area(sq.mi)"]
    df_state_area = DataFrame(rows, columns=cols)
    print(df_state_area)
    print(df_state_area.shape)


def create_state_population():
    rows = [
        ["AL", "under 18", "2020", 1117489.0], ["AL", "total", "2020", 4817528.0],

    ]


if __name__ == '__main__':
    create_state_abbrevs()
    create_state_area()
