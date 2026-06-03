---
search:
  boost: 10.0
---

# Class: OfficialAuthorityExerciseImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with the exercise of official_

_authorities_



<div data-search-exclude markdown="1">



URI: [justifications:OfficialAuthorityExerciseImpaired](https://w3id.org/lmodel/dpv/justifications/OfficialAuthorityExerciseImpaired)





```mermaid
 classDiagram
    class OfficialAuthorityExerciseImpaired
    click OfficialAuthorityExerciseImpaired href "../OfficialAuthorityExerciseImpaired/"
      LegalProcessImpaired <|-- OfficialAuthorityExerciseImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **OfficialAuthorityExerciseImpaired**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:OfficialAuthorityExerciseImpaired](https://w3id.org/lmodel/dpv/justifications/OfficialAuthorityExerciseImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Official Authority Exercise Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#OfficialAuthorityExerciseImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:OfficialAuthorityExerciseImpaired |
| native | justifications:OfficialAuthorityExerciseImpaired |
| exact | dpv_justifications:OfficialAuthorityExerciseImpaired, dpv_justifications_owl:OfficialAuthorityExerciseImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OfficialAuthorityExerciseImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#OfficialAuthorityExerciseImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the exercise of official

  authorities'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Official Authority Exercise Impaired
exact_mappings:
- dpv_justifications:OfficialAuthorityExerciseImpaired
- dpv_justifications_owl:OfficialAuthorityExerciseImpaired
is_a: LegalProcessImpaired
class_uri: justifications:OfficialAuthorityExerciseImpaired

```
</details>

### Induced

<details>
```yaml
name: OfficialAuthorityExerciseImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#OfficialAuthorityExerciseImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the exercise of official

  authorities'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Official Authority Exercise Impaired
exact_mappings:
- dpv_justifications:OfficialAuthorityExerciseImpaired
- dpv_justifications_owl:OfficialAuthorityExerciseImpaired
is_a: LegalProcessImpaired
class_uri: justifications:OfficialAuthorityExerciseImpaired

```
</details></div>