---
search:
  boost: 10.0
---

# Class: DefenceImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with necessary tasks to safeguard_

_defence_



<div data-search-exclude markdown="1">



URI: [justifications:DefenceImpaired](https://w3id.org/lmodel/dpv/justifications/DefenceImpaired)





```mermaid
 classDiagram
    class DefenceImpaired
    click DefenceImpaired href "../DefenceImpaired/"
      SecurityImpaired <|-- DefenceImpaired
        click SecurityImpaired href "../SecurityImpaired/"
      LegalProcessImpaired <|-- DefenceImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **DefenceImpaired** [ [SecurityImpaired](SecurityImpaired.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:DefenceImpaired](https://w3id.org/lmodel/dpv/justifications/DefenceImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Defence Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#DefenceImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:DefenceImpaired |
| native | justifications:DefenceImpaired |
| exact | dpv_justifications:DefenceImpaired, dpv_justifications_owl:DefenceImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DefenceImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#DefenceImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with necessary tasks to safeguard

  defence'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Defence Impaired
exact_mappings:
- dpv_justifications:DefenceImpaired
- dpv_justifications_owl:DefenceImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:DefenceImpaired

```
</details>

### Induced

<details>
```yaml
name: DefenceImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#DefenceImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with necessary tasks to safeguard

  defence'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Defence Impaired
exact_mappings:
- dpv_justifications:DefenceImpaired
- dpv_justifications_owl:DefenceImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:DefenceImpaired

```
</details></div>