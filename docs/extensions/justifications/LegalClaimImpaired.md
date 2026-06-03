---
search:
  boost: 10.0
---

# Class: LegalClaimImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would impair the establishment, exercise, or_

_defence of a legal claim_



<div data-search-exclude markdown="1">



URI: [justifications:LegalClaimImpaired](https://w3id.org/lmodel/dpv/justifications/LegalClaimImpaired)





```mermaid
 classDiagram
    class LegalClaimImpaired
    click LegalClaimImpaired href "../LegalClaimImpaired/"
      LegalProcessImpaired <|-- LegalClaimImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      

      LegalClaimImpaired <|-- LegalClaimDefenceImpaired
        click LegalClaimDefenceImpaired href "../LegalClaimDefenceImpaired/"
      LegalClaimImpaired <|-- LegalClaimEstablishmentImpaired
        click LegalClaimEstablishmentImpaired href "../LegalClaimEstablishmentImpaired/"
      LegalClaimImpaired <|-- LegalClaimExerciseImpaired
        click LegalClaimExerciseImpaired href "../LegalClaimExerciseImpaired/"
      

      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **LegalClaimImpaired**
            * [LegalClaimDefenceImpaired](LegalClaimDefenceImpaired.md)
            * [LegalClaimEstablishmentImpaired](LegalClaimEstablishmentImpaired.md)
            * [LegalClaimExerciseImpaired](LegalClaimExerciseImpaired.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:LegalClaimImpaired](https://w3id.org/lmodel/dpv/justifications/LegalClaimImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Legal Claim Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#LegalClaimImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:LegalClaimImpaired |
| native | justifications:LegalClaimImpaired |
| exact | dpv_justifications:LegalClaimImpaired, dpv_justifications_owl:LegalClaimImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LegalClaimImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegalClaimImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would impair the establishment, exercise, or

  defence of a legal claim'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Legal Claim Impaired
exact_mappings:
- dpv_justifications:LegalClaimImpaired
- dpv_justifications_owl:LegalClaimImpaired
is_a: LegalProcessImpaired
class_uri: justifications:LegalClaimImpaired

```
</details>

### Induced

<details>
```yaml
name: LegalClaimImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegalClaimImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would impair the establishment, exercise, or

  defence of a legal claim'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Legal Claim Impaired
exact_mappings:
- dpv_justifications:LegalClaimImpaired
- dpv_justifications_owl:LegalClaimImpaired
is_a: LegalProcessImpaired
class_uri: justifications:LegalClaimImpaired

```
</details></div>