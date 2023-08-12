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

    new_movie_preference = -1

    while new_movie_preference not in np.arange(0, 8):
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
        else:
            print("Opção inválida, tente novamente")


def init_fuzzy_sets():
    # Antecedentes
    genre = ctrl.Antecedent(np.arange(1, 11), "genre")
    user_rating = ctrl.Antecedent(np.arange(1, 11), "user_rating")
    cast = ctrl.Antecedent(np.arange(1, 11), "cast")
    director = ctrl.Antecedent(np.arange(1, 11), "director")
    popularity = ctrl.Antecedent(np.arange(1, 11), "popularity")

    # Consequente, representando o grau de recomendação do filme de terror
    recommendation_score = ctrl.Consequent(
        np.arange(1, 11), "recommendation_score", defuzzify_method="mom"
    )

    return pertinence_levels(
        genre, user_rating, cast, director, popularity, recommendation_score
    )


def pertinence_levels(
    genre, user_rating, cast, director, popularity, recommendation_score
):
    # Níveis de pertinência de genero: baixo, média e alto
    genre["baixo"] = fuzz.trapmf(genre.universe, [0, 0, 4, 5])
    genre["medio"] = fuzz.trapmf(genre.universe, [4, 5, 6, 8])
    genre["alto"] = fuzz.trapmf(genre.universe, [7, 8, 10, 10])

    # Níveis de pertinência (baixo, média e alto) de nota do usuário considerando os conjuntos fuzzy: ruim, médio, bom e ótimo
    user_rating["ruim"] = fuzz.trapmf(user_rating.universe, [0, 0, 3, 4])
    user_rating["medio"] = fuzz.trimf(user_rating.universe, [3, 5, 7])
    user_rating["bom"] = fuzz.trimf(user_rating.universe, [5, 7, 9])
    user_rating["otimo"] = fuzz.trapmf(user_rating.universe, [7, 9, 10, 10])

    # Níveis de pertinência (baixo, média e alto) de popularidade considerando os conjuntos fuzzy: baixo, média e alto
    popularity["baixo"] = fuzz.trapmf(popularity.universe, [0, 0, 2, 4])
    popularity["medio"] = fuzz.trimf(popularity.universe, [3, 5, 7])
    popularity["alto"] = fuzz.trapmf(popularity.universe, [6, 8, 10, 10])

    # Níveis de pertinência (baixo, média e alto) do elenco considerando os conjuntos fuzzy: desconhecido, conhecido e famoso
    cast["desconhecido"] = fuzz.trapmf(cast.universe, [0, 0, 2, 5])
    cast["conhecido"] = fuzz.trapmf(cast.universe, [3, 5, 6, 8])
    cast["famoso"] = fuzz.trapmf(cast.universe, [6, 8, 10, 10])

    # Níveis de pertinência (baixo, média e alto) do diretor considerando os conjuntos fuzzy: desconhecido, conhecido e famoso
    director["desconhecido"] = fuzz.trapmf(director.universe, [0, 0, 2, 4])
    director["conhecido"] = fuzz.trimf(director.universe, [3, 5, 7])
    director["famoso"] = fuzz.trapmf(director.universe, [5, 8, 10, 10])

    # Níveis de pertinência (baixo, média e alto) da recomendação considerando os conjuntos fuzzy: não recomendar e recomendar
    recommendation_score["nao_recomendar"] = fuzz.trapmf(
        recommendation_score.universe, [0, 0, 3, 6]
    )
    recommendation_score["recomendar"] = fuzz.trapmf(
        recommendation_score.universe, [4, 8, 10, 10]
    )

    return genre, user_rating, cast, director, popularity, recommendation_score


def configure_rules(
    genre, user_rating, cast, director, popularity, recommendation_score
):
    rules_list = []

    rules_list.append(
        ctrl.Rule(
            genre["baixo"] & user_rating["ruim"], recommendation_score["nao_recomendar"]
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["baixo"] & user_rating["medio"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["baixo"] & user_rating["bom"], recommendation_score["nao_recomendar"]
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["baixo"] & user_rating["otimo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["baixo"] & cast["desconhecido"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["baixo"] & cast["conhecido"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["baixo"] & cast["famoso"], recommendation_score["nao_recomendar"]
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["baixo"] & popularity["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["baixo"] & popularity["medio"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["baixo"] & popularity["alto"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["baixo"] & director["desconhecido"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["baixo"] & director["conhecido"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["baixo"] & director["famoso"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["medio"] & user_rating["ruim"], recommendation_score["nao_recomendar"]
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["medio"] & user_rating["medio"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["medio"] & user_rating["bom"], recommendation_score["recomendar"]
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["medio"] & user_rating["otimo"], recommendation_score["recomendar"]
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["alto"] & user_rating["ruim"], recommendation_score["nao_recomendar"]
        )
    )

    rules_list.append(
        ctrl.Rule(
            genre["alto"] & user_rating["medio"], recommendation_score["recomendar"]
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["alto"] & user_rating["bom"], recommendation_score["recomendar"]
        )
    )
    rules_list.append(
        ctrl.Rule(
            genre["alto"] & user_rating["otimo"], recommendation_score["recomendar"]
        )
    )

    # Separação
    rules_list.append(
        ctrl.Rule(
            popularity["baixo"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["baixo"] & user_rating["medio"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["baixo"] & user_rating["bom"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["baixo"] & user_rating["otimo"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["medio"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["medio"] & user_rating["medio"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["medio"] & user_rating["bom"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["medio"] & user_rating["otimo"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["alto"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["alto"] & user_rating["medio"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["alto"] & user_rating["bom"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["alto"] & user_rating["otimo"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )

    # Separação
    rules_list.append(
        ctrl.Rule(
            cast["desconhecido"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["desconhecido"] & user_rating["medio"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["desconhecido"] & user_rating["bom"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["desconhecido"] & user_rating["otimo"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["conhecido"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["conhecido"] & user_rating["medio"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["conhecido"] & user_rating["bom"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["conhecido"] & user_rating["otimo"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["famoso"] & user_rating["ruim"], recommendation_score["nao_recomendar"]
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["famoso"] & user_rating["medio"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["famoso"] & user_rating["bom"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["famoso"] & user_rating["otimo"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )

    # Separação
    rules_list.append(
        ctrl.Rule(
            director["desconhecido"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["desconhecido"] & user_rating["medio"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["desconhecido"] & user_rating["bom"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["desconhecido"] & user_rating["otimo"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["conhecido"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["conhecido"] & user_rating["medio"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["conhecido"] & user_rating["bom"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["conhecido"] & user_rating["otimo"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["famoso"] & user_rating["ruim"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["famoso"] & user_rating["medio"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["famoso"] & user_rating["bom"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["famoso"] & user_rating["otimo"] & ~genre["baixo"],
            recommendation_score["recomendar"],
        )
    )

    # Separação
    rules_list.append(
        ctrl.Rule(
            director["desconhecido"] & user_rating["ruim"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["desconhecido"] & user_rating["medio"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["desconhecido"] & user_rating["bom"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["desconhecido"] & user_rating["otimo"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["conhecido"] & user_rating["ruim"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["conhecido"] & user_rating["medio"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["conhecido"] & user_rating["bom"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["conhecido"] & user_rating["otimo"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["famoso"] & user_rating["ruim"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["famoso"] & user_rating["medio"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["famoso"] & user_rating["bom"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            director["famoso"] & user_rating["otimo"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )

    # Separação
    rules_list.append(
        ctrl.Rule(
            cast["desconhecido"] & user_rating["ruim"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["desconhecido"] & user_rating["medio"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["desconhecido"] & user_rating["bom"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["desconhecido"] & user_rating["otimo"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["conhecido"] & user_rating["ruim"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["conhecido"] & user_rating["medio"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["conhecido"] & user_rating["bom"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["conhecido"] & user_rating["otimo"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["famoso"] & user_rating["ruim"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["famoso"] & user_rating["medio"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["famoso"] & user_rating["bom"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            cast["famoso"] & user_rating["otimo"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )

    # Separação
    rules_list.append(
        ctrl.Rule(
            popularity["baixo"] & user_rating["ruim"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["baixo"] & user_rating["medio"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["baixo"] & user_rating["bom"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["baixo"] & user_rating["otimo"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["medio"] & user_rating["ruim"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["medio"] & user_rating["medio"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["medio"] & user_rating["bom"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["medio"] & user_rating["otimo"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["alto"] & user_rating["ruim"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["alto"] & user_rating["medio"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["alto"] & user_rating["bom"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )
    rules_list.append(
        ctrl.Rule(
            popularity["alto"] & user_rating["otimo"] & genre["baixo"],
            recommendation_score["nao_recomendar"],
        )
    )

    return rules_list


def fuzzy_configurations():
    (
        genre,
        user_rating,
        cast,
        director,
        popularity,
        recommendation_score,
    ) = init_fuzzy_sets()
    recommendation_ctrl = ctrl.ControlSystem(
        configure_rules(
            genre, user_rating, cast, director, popularity, recommendation_score
        )
    )
    recommendation = ctrl.ControlSystemSimulation(recommendation_ctrl)
    return recommendation, recommendation_score


def menu():
    user_option = 0
    actual_movie_preference = None
    movie_data = None

    recommendation, recommendation_score = fuzzy_configurations()
    while user_option != 4:
        print(f"Preferencia do usuário: {actual_movie_preference}\n")

        print("Sistema de recomendação de filmes")
        print("1 - Gerenciar perfil de filme do usuário")
        print("2 - Inserir dados do filme")
        print("3 - Iniciar recomendação")
        print("4 - Sair")

        user_option = int(input("Digite a opção desejada: "))

        match user_option:
            case 1:
                actual_movie_preference = manage_user_movie_preference(
                    actual_movie_preference
                )
            case 2:
                if actual_movie_preference is None:
                    print(
                        "É necessário gerenciar o perfil de filme do usuário primeiro\n"
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
            case 3:
                if movie_data is None:
                    print("É necessário inserir os dados do filme primeiro\n")
                else:
                    recommendation.compute()
                    print(
                        f"nGrau de pertinência para o filme ser recomendado: {recommendation.output['recommendation_score']}"
                    )
                    recommendation_score.view(sim=recommendation)
            case 4:
                exit()
            case _:
                print("Opção inválida\n")


if __name__ == "__main__":
    menu()
