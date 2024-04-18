DATA_PENYAKIT = {
    "batuk": (["batuk", "sakit_tenggorokan"], [1.0, 0.6]),
    "flu_ringan": (["batuk", "demam", "pilek"], [0.4, 0.6, 0.8]),
    "flu_berat": (
        ["batuk", "demam", "pilek", "sakit_tenggorokan", "bersin"],
        [0.4, 0.6, 0.6, 0.4, 0.8],
    ),
}

def hitung_nilai_probalitas(gejala_user: list[str]):
    posterior_prob = 0.0
    penyakit_prob = ""

    for penyakit, (gejala_penyakit, prob_penyakit) in DATA_PENYAKIT.items():
        n_nilai_semesta = 0.0
        prob_gejala = []

        for gejala in gejala_user:
            if gejala in gejala_penyakit:
                _index_gejala = gejala_penyakit.index(gejala)
                prob_gejala.append(prob_penyakit[_index_gejala])
                n_nilai_semesta += prob_penyakit[_index_gejala]

        nilai_semesta_p_gejala = []
        for i in range(0, len(prob_gejala)):
            p_H = prob_gejala[i] / n_nilai_semesta
            nilai_semesta_p_gejala.append(p_H)

        p_gejala = []
        n_p_gejala = 0.0
        for i in range(0, len(nilai_semesta_p_gejala)):
            p_gejala.append(nilai_semesta_p_gejala[i] * prob_gejala[i])
            n_p_gejala += nilai_semesta_p_gejala[i] * prob_gejala[i]

        n_p_gejala_penyakit = 0
        for i in range(0, len(p_gejala)):
            p_gejala_penyakit = p_gejala[i] * prob_gejala[i] / n_p_gejala
            n_p_gejala_penyakit += p_gejala_penyakit

        print(penyakit, n_p_gejala_penyakit)

        if n_p_gejala_penyakit > posterior_prob:
            posterior_prob = max(posterior_prob, n_p_gejala_penyakit)
            penyakit_prob = penyakit

    return penyakit_prob, posterior_prob

input_user = ['demam', 'pilek', 'bersin']
probalitas = hitung_nilai_probalitas(input_user)
print('hasil diagnosa :', probalitas)
