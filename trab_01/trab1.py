import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import itertools


def insert_movie_data(actual_movie_preference):
    print("\nInsira os dados do filme: ")
    print(
        f"De 1 a 10, o quanto o filme é de considerado do gênero {actual_movie_preference}?"
    )
    genre_input = int(input())
    print("De 1 a 10, qual a nota dos usuários para o filme?")
    user_rating_input = int(input())
    print("De 1 a 10, qual o nível de popularidade do filme?")
    popularity_input = int(input())
    print("De 1 a 10, o quão famoso é o elenco do filme?")
    cast_input = int(input())
    print("De 1 a 10, o quão conhecido é o diretor do filme?")
    director_input = int(input())

    return genre_input, user_rating_input, popularity_input, cast_input, director_input


def manage_user_movie_preference(user_movie_preference):
    movie_type_list = [
        "Ação",
        "Comédia",
        "Drama",
        "Romance",
        "Ficção científica",
        "Terror",
        "Animação",
    ]
    print("\nSelecione a prefêrencia de filme: ")
    print("0 - Voltar")

    for i, movie_type in enumerate(movie_type_list):
        i += 1
        print(f"{i} - {movie_type}")

    new_movie_preference = int(input())

    if new_movie_preference == 0:
        return user_movie_preference
    elif new_movie_preference in np.arange(1, 8):
        return movie_type_list[new_movie_preference - 1]


def menu(
    user_movie_preference=None,
    is_first_time=False,
    genre=None,
    user_rating=None,
    cast=None,
    director=None,
    popularity=None,
    recommendation_score=None,
    recommendation=None,
    movie_data=None,
):
    print(f"Preferencia do usuário: {user_movie_preference}\n")
    actual_movie_preference = user_movie_preference

    if is_first_time:
        genre = ctrl.Antecedent(np.arange(1, 11), "genre")
        user_rating = ctrl.Antecedent(np.arange(1, 11), "user_rating")
        cast = ctrl.Antecedent(np.arange(1, 11), "cast")
        director = ctrl.Antecedent(np.arange(1, 11), "director")
        popularity = ctrl.Antecedent(np.arange(1, 11), "popularity")

        # Consequente, representando o grau de recomendação do filme de terror
        recommendation_score = ctrl.Consequent(np.arange(1, 11), "recommendation_score")

        user_option = 0

        # Níveis de pertinência de genero: baixa, média e alta
        genre["baixo"] = fuzz.trapmf(genre.universe, [0, 0, 3, 5])
        genre["medio"] = fuzz.trapmf(genre.universe, [3, 5, 6, 8])
        genre["alto"] = fuzz.trapmf(genre.universe, [6, 8, 10, 10])

        # Níveis de pertinência (baixa, média e alta) de nota do usuário considerando os conjuntos fuzzy: ruim, médio, bom e ótimo
        user_rating["ruim"] = fuzz.trapmf(user_rating.universe, [0, 0, 3, 4])
        user_rating["medio"] = fuzz.trimf(user_rating.universe, [3, 5, 7])
        user_rating["bom"] = fuzz.trimf(user_rating.universe, [5, 7, 9])
        user_rating["otimo"] = fuzz.trapmf(user_rating.universe, [7, 9, 10, 10])

        # Níveis de pertinência (baixa, média e alta) de popularidade considerando os conjuntos fuzzy: baixa, média e alta
        popularity["baixa"] = fuzz.trapmf(popularity.universe, [0, 0, 2, 4])
        popularity["media"] = fuzz.trimf(popularity.universe, [3, 5, 7])
        popularity["alta"] = fuzz.trapmf(popularity.universe, [6, 8, 10, 10])

        # Níveis de pertinência (baixa, média e alta) do elenco considerando os conjuntos fuzzy: desconhecido, conhecido e famoso
        cast["desconhecido"] = fuzz.trapmf(cast.universe, [0, 0, 2, 5])
        cast["conhecido"] = fuzz.trapmf(cast.universe, [3, 5, 6, 8])
        cast["famoso"] = fuzz.trapmf(cast.universe, [6, 8, 10, 10])

        # Níveis de pertinência (baixa, média e alta) do diretor considerando os conjuntos fuzzy: desconhecido, conhecido e famoso
        director["desconhecido"] = fuzz.trapmf(director.universe, [0, 0, 2, 4])
        director["conhecido"] = fuzz.trimf(director.universe, [3, 5, 7])
        director["famoso"] = fuzz.trapmf(director.universe, [5, 8, 10, 10])

        # Níveis de pertinência (baixa, média e alta) da recomendação considerando os conjuntos fuzzy: não recomendar e recomendar
        recommendation_score["nao_recomendar"] = fuzz.trapmf(
            recommendation_score.universe, [0, 0, 3, 6]
        )
        recommendation_score["recomendar"] = fuzz.trapmf(
            recommendation_score.universe, [3, 5, 10, 10]
        )

        # Regras
        # rule_list = []
        # variables_list = [genre, user_rating, popularity, cast, director]

        # rule_conditions = [
        #     ["baixo", "medio", "alto"],
        #     ["ruim", "medio", "bom", "otimo"],
        #     ["baixa", "media", "alta"],
        #     ["desconhecido", "conhecido", "famoso"],
        #     ["desconhecido", "conhecido", "famoso"],
        # ]

        # rule_combinations = list(itertools.product(*rule_conditions))

        # rules = []
        # for i, combination in enumerate(rule_combinations):
        #     antecedents = [var[rule] for var, rule in zip(variables_list, combination)]
        #     print(antecedents)
        #     print(i)
        # recommendation = recommendation_score["recomendar"]
        # rule = ctrl.Rule(antecedents, recommendation)
        # rules.append(rule)

        # print(rules)

        rule1 = ctrl.Rule(
            genre["baixo"] & user_rating["ruim"], recommendation_score["nao_recomendar"]
        )
        rule2 = ctrl.Rule(
            genre["baixo"] & user_rating["medio"],
            recommendation_score["nao_recomendar"],
        )
        rule3 = ctrl.Rule(
            genre["baixo"] & user_rating["bom"], recommendation_score["nao_recomendar"]
        )
        rule4 = ctrl.Rule(
            genre["baixo"] & user_rating["otimo"],
            recommendation_score["nao_recomendar"],
        )
        rule5 = ctrl.Rule(
            genre["medio"] & user_rating["ruim"], recommendation_score["nao_recomendar"]
        )
        rule6 = ctrl.Rule(
            genre["medio"] & user_rating["medio"],
            recommendation_score["nao_recomendar"],
        )
        rule7 = ctrl.Rule(
            genre["medio"] & user_rating["bom"], recommendation_score["recomendar"]
        )
        rule8 = ctrl.Rule(
            genre["medio"] & user_rating["otimo"], recommendation_score["recomendar"]
        )
        rule9 = ctrl.Rule(
            genre["alto"] & user_rating["ruim"], recommendation_score["nao_recomendar"]
        )
        rule10 = ctrl.Rule(
            genre["alto"] & user_rating["medio"], recommendation_score["recomendar"]
        )
        rule11 = ctrl.Rule(
            genre["alto"] & user_rating["bom"], recommendation_score["recomendar"]
        )
        rule12 = ctrl.Rule(
            genre["alto"] & user_rating["otimo"], recommendation_score["recomendar"]
        )

        rule13 = ctrl.Rule(
            popularity["baixa"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
        rule14 = ctrl.Rule(
            popularity["baixa"] & user_rating["medio"],
            recommendation_score["nao_recomendar"],
        )
        rule15 = ctrl.Rule(
            popularity["baixa"] & user_rating["bom"], recommendation_score["recomendar"]
        )
        rule16 = ctrl.Rule(
            popularity["baixa"] & user_rating["otimo"],
            recommendation_score["recomendar"],
        )
        rule17 = ctrl.Rule(
            popularity["media"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
        rule18 = ctrl.Rule(
            popularity["media"] & user_rating["medio"],
            recommendation_score["recomendar"],
        )
        rule19 = ctrl.Rule(
            popularity["media"] & user_rating["bom"], recommendation_score["recomendar"]
        )
        rule20 = ctrl.Rule(
            popularity["media"] & user_rating["otimo"],
            recommendation_score["recomendar"],
        )
        rule21 = ctrl.Rule(
            popularity["alta"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
        rule22 = ctrl.Rule(
            popularity["alta"] & user_rating["medio"],
            recommendation_score["recomendar"],
        )
        rule23 = ctrl.Rule(
            popularity["alta"] & user_rating["bom"], recommendation_score["recomendar"]
        )

        rule24 = ctrl.Rule(
            cast["desconhecido"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
        rule25 = ctrl.Rule(
            cast["desconhecido"] & user_rating["medio"],
            recommendation_score["nao_recomendar"],
        )
        rule26 = ctrl.Rule(
            cast["desconhecido"] & user_rating["bom"],
            recommendation_score["recomendar"],
        )
        rule27 = ctrl.Rule(
            cast["desconhecido"] & user_rating["otimo"],
            recommendation_score["recomendar"],
        )
        rule28 = ctrl.Rule(
            cast["conhecido"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
        rule29 = ctrl.Rule(
            cast["conhecido"] & user_rating["medio"], recommendation_score["recomendar"]
        )
        rule30 = ctrl.Rule(
            cast["conhecido"] & user_rating["bom"], recommendation_score["recomendar"]
        )
        rule31 = ctrl.Rule(
            cast["conhecido"] & user_rating["otimo"], recommendation_score["recomendar"]
        )
        rule32 = ctrl.Rule(
            cast["famoso"] & user_rating["ruim"], recommendation_score["nao_recomendar"]
        )
        rule33 = ctrl.Rule(
            cast["famoso"] & user_rating["medio"], recommendation_score["recomendar"]
        )
        rule34 = ctrl.Rule(
            cast["famoso"] & user_rating["bom"], recommendation_score["recomendar"]
        )
        rule35 = ctrl.Rule(
            cast["famoso"] & user_rating["otimo"], recommendation_score["recomendar"]
        )

        rule36 = ctrl.Rule(
            director["desconhecido"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
        rule37 = ctrl.Rule(
            director["desconhecido"] & user_rating["medio"],
            recommendation_score["nao_recomendar"],
        )
        rule38 = ctrl.Rule(
            director["desconhecido"] & user_rating["bom"],
            recommendation_score["recomendar"],
        )
        rule39 = ctrl.Rule(
            director["desconhecido"] & user_rating["otimo"],
            recommendation_score["recomendar"],
        )
        rule40 = ctrl.Rule(
            director["conhecido"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
        rule41 = ctrl.Rule(
            director["conhecido"] & user_rating["medio"],
            recommendation_score["recomendar"],
        )
        rule42 = ctrl.Rule(
            director["conhecido"] & user_rating["bom"],
            recommendation_score["recomendar"],
        )
        rule43 = ctrl.Rule(
            director["conhecido"] & user_rating["otimo"],
            recommendation_score["recomendar"],
        )
        rule44 = ctrl.Rule(
            director["famoso"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
        rule45 = ctrl.Rule(
            director["famoso"] & user_rating["medio"],
            recommendation_score["recomendar"],
        )
        rule46 = ctrl.Rule(
            director["famoso"] & user_rating["bom"], recommendation_score["recomendar"]
        )
        rule47 = ctrl.Rule(
            director["famoso"] & user_rating["otimo"],
            recommendation_score["recomendar"],
        )

        recommendation_ctrl = ctrl.ControlSystem(
            [
                rule1,
                rule2,
                rule3,
                rule4,
                rule5,
                rule6,
                rule7,
                rule8,
                rule9,
                rule10,
                rule11,
                rule12,
                rule13,
                rule14,
                rule15,
                rule16,
                rule17,
                rule18,
                rule19,
                rule20,
                rule21,
                rule22,
                rule23,
                rule24,
                rule25,
                rule26,
                rule27,
                rule28,
                rule29,
                rule30,
                rule31,
                rule32,
                rule33,
                rule34,
                rule35,
                rule36,
                rule37,
                rule38,
                rule39,
                rule40,
                rule41,
                rule42,
                rule43,
                rule44,
                rule45,
                rule46,
                rule47,
            ]
        )

        recommendation = ctrl.ControlSystemSimulation(recommendation_ctrl)

    print("Sistema de recomendação de filmes")
    print("1 - Gerenciar perfil de filme do usuário")
    print("2 - Inserir dados do filme")
    print("3 - Iniciar recomendação")
    print("4 - Sair")

    user_option = int(input("Digite a opção desejada: "))
    match user_option:
        case 1:
            actual_movie_preference = manage_user_movie_preference(
                user_movie_preference
            )
            return menu(
                actual_movie_preference,
                genre=genre,
                cast=cast,
                director=director,
                user_rating=user_rating,
                popularity=popularity,
                recommendation_score=recommendation_score,
                recommendation=recommendation,
                movie_data=movie_data,
            )
        case 2:
            if actual_movie_preference is None:
                print("É necessário gerenciar o perfil de filme do usuário primeiro\n")
                return menu(
                    user_movie_preference,
                    genre=genre,
                    cast=cast,
                    director=director,
                    user_rating=user_rating,
                    popularity=popularity,
                    recommendation_score=recommendation_score,
                    recommendation=recommendation,
                    movie_data=movie_data,
                )
            else:
                movie_data = insert_movie_data(actual_movie_preference)
                print(movie_data)
                variables = [
                    "genre",
                    "user_rating",
                    "popularity",
                    "cast",
                    "director",
                ]

                for i, variable in enumerate(variables):
                    print(movie_data[i])
                    recommendation.input[variable] = movie_data[i]
                return menu(
                    user_movie_preference,
                    genre=genre,
                    cast=cast,
                    director=director,
                    user_rating=user_rating,
                    popularity=popularity,
                    recommendation_score=recommendation_score,
                    recommendation=recommendation,
                    movie_data=movie_data,
                )
        case 3:
            if movie_data is None:
                print("É necessário inserir os dados do filme primeiro\n")
                return menu(
                    user_movie_preference,
                    genre=genre,
                    cast=cast,
                    director=director,
                    user_rating=user_rating,
                    popularity=popularity,
                    recommendation_score=recommendation_score,
                    recommendation=recommendation,
                    movie_data=movie_data,
                )
            recommendation.compute()
            print(f"nGrau de pertinência para o filme ser recomendado: {recommendation.output['recommendation_score']}")
            recommendation_score.view(sim=recommendation)
            return menu(
                user_movie_preference,
                genre=genre,
                cast=cast,
                director=director,
                user_rating=user_rating,
                popularity=popularity,
                recommendation_score=recommendation_score,
                recommendation=recommendation,
                movie_data=movie_data,
            )
        case 4:
            exit()
        case _:
            print("Opção inválida\n")
            menu(
                user_movie_preference,
                genre=genre,
                cast=cast,
                director=director,
                user_rating=user_rating,
                popularity=popularity,
                recommendation_score=recommendation_score,
                recommendation=recommendation,
                movie_data=movie_data,
            )


if __name__ == "__main__":
    menu(is_first_time=True)
