---
search:
  boost: 10.0
---

# Class: FulfilmentImpossible 


_Justification that the process could not be fulfilled or was not_

_successful because it is impossible to fulfil_



<div data-search-exclude markdown="1">



URI: [justifications:FulfilmentImpossible](https://w3id.org/lmodel/dpv/justifications/FulfilmentImpossible)





```mermaid
 classDiagram
    class FulfilmentImpossible
    click FulfilmentImpossible href "../FulfilmentImpossible/"
      NonFulfilmentJustification <|-- FulfilmentImpossible
        click NonFulfilmentJustification href "../NonFulfilmentJustification/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * **FulfilmentImpossible**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:FulfilmentImpossible](https://w3id.org/lmodel/dpv/justifications/FulfilmentImpossible) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Fulfilment Impossible




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#FulfilmentImpossible |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:FulfilmentImpossible |
| native | justifications:FulfilmentImpossible |
| exact | dpv_justifications:FulfilmentImpossible, dpv_justifications_owl:FulfilmentImpossible |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FulfilmentImpossible
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#FulfilmentImpossible
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it is impossible to fulfil'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Fulfilment Impossible
exact_mappings:
- dpv_justifications:FulfilmentImpossible
- dpv_justifications_owl:FulfilmentImpossible
is_a: NonFulfilmentJustification
class_uri: justifications:FulfilmentImpossible

```
</details>

### Induced

<details>
```yaml
name: FulfilmentImpossible
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#FulfilmentImpossible
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it is impossible to fulfil'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Fulfilment Impossible
exact_mappings:
- dpv_justifications:FulfilmentImpossible
- dpv_justifications_owl:FulfilmentImpossible
is_a: NonFulfilmentJustification
class_uri: justifications:FulfilmentImpossible

```
</details></div>