# Todos os casos possíveis de regras para o sistema fuzzy (incompleto)
rules_list = []

rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)

rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["media"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)

# Separação
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["baixo"]
        & popularity["alta"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["nao_recomendar"],
    )
)

# Separação
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)

# Separação
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)

# Separação
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)

# Separação
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["baixa"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)

# Separação
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["media"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)

# Separação
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["desconhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["conhecido"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["ruim"],
        recommendation_score["nao_recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["desconhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["ruim"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["conhecido"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["ruim"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["medio"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["bom"],
        recommendation_score["recomendar"],
    )
)
rules_list.append(
    ctrl.Rule(
        genre["medio"]
        & popularity["alta"]
        & cast["famoso"]
        & director["famoso"]
        & user_rating["otimo"],
        recommendation_score["recomendar"],
    )
)
