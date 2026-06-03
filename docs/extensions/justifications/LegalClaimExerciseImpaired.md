---
search:
  boost: 10.0
---

# Class: LegalClaimExerciseImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with the exercise of legal claims_



<div data-search-exclude markdown="1">



URI: [justifications:LegalClaimExerciseImpaired](https://w3id.org/lmodel/dpv/justifications/LegalClaimExerciseImpaired)





```mermaid
 classDiagram
    class LegalClaimExerciseImpaired
    click LegalClaimExerciseImpaired href "../LegalClaimExerciseImpaired/"
      LegalClaimImpaired <|-- LegalClaimExerciseImpaired
        click LegalClaimImpaired href "../LegalClaimImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * [LegalClaimImpaired](LegalClaimImpaired.md)
            * **LegalClaimExerciseImpaired**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:LegalClaimExerciseImpaired](https://w3id.org/lmodel/dpv/justifications/LegalClaimExerciseImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Legal Claim Exercise Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#LegalClaimExerciseImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:LegalClaimExerciseImpaired |
| native | justifications:LegalClaimExerciseImpaired |
| exact | dpv_justifications:LegalClaimExerciseImpaired, dpv_justifications_owl:LegalClaimExerciseImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LegalClaimExerciseImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegalClaimExerciseImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the exercise of legal claims'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Legal Claim Exercise Impaired
exact_mappings:
- dpv_justifications:LegalClaimExerciseImpaired
- dpv_justifications_owl:LegalClaimExerciseImpaired
is_a: LegalClaimImpaired
class_uri: justifications:LegalClaimExerciseImpaired

```
</details>

### Induced

<details>
```yaml
name: LegalClaimExerciseImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#LegalClaimExerciseImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the exercise of legal claims'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Legal Claim Exercise Impaired
exact_mappings:
- dpv_justifications:LegalClaimExerciseImpaired
- dpv_justifications_owl:LegalClaimExerciseImpaired
is_a: LegalClaimImpaired
class_uri: justifications:LegalClaimExerciseImpaired

```
</details></div>