def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += " dan " + value
        else:
            merged_dict[key] = value
    return merged_dict


jadwalDasproIf2 = {
    'Senin': 'Daspro',
}

jadwalDasproIf3 = {
    'Kamis': 'Daspro',
}


hasil_gabung = merge_dicts(jadwalDasproIf2, jadwalDasproIf3)


print("Hasil penggabungan dua data dictionary:")
print(hasil_gabung)


