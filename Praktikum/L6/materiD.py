# D
DATA_PENYAKIT = {
    "kulit normal": (
        ["G001", "G002" "G003", "G004", "G005", "G006", "G011"],
        [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
    ),
    "kulit bermiyak": (
        ["G001", "G008", "G009", "G016"],
        [0.8, 0.8, 0.8, 0.8],
    ),
    "kulit kering": (
        ["G001", "G005", "G010", "G011", "G012"],
        [0.6, 0.6, 0.8, 0.6, 0.6],
    ),
    "kulit kombinasi": (
        ["G007", "G014", "G015", "G016", "G017"],
        [0.6, 0.4, 0.6, 0.4, 0.6],
    ),
    "kulit sensitif": (
        ["G012", "G018", "G019", "G020"],
        [0.8, 0.8, 0.8, 0.8],
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
