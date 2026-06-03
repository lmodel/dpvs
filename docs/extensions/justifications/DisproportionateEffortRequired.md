---
search:
  boost: 10.0
---

# Class: DisproportionateEffortRequired 


_Justification that the process could not be fulfilled or was not_

_successful because it requires a disproportionate effort_



<div data-search-exclude markdown="1">



URI: [justifications:DisproportionateEffortRequired](https://w3id.org/lmodel/dpv/justifications/DisproportionateEffortRequired)





```mermaid
 classDiagram
    class DisproportionateEffortRequired
    click DisproportionateEffortRequired href "../DisproportionateEffortRequired/"
      NonFulfilmentJustification <|-- DisproportionateEffortRequired
        click NonFulfilmentJustification href "../NonFulfilmentJustification/"
      

      DisproportionateEffortRequired <|-- EntityAlreadyInformed
        click EntityAlreadyInformed href "../EntityAlreadyInformed/"
      

      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * **DisproportionateEffortRequired**
        * [EntityAlreadyInformed](EntityAlreadyInformed.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:DisproportionateEffortRequired](https://w3id.org/lmodel/dpv/justifications/DisproportionateEffortRequired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Disproportionate Effort Required




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#DisproportionateEffortRequired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:DisproportionateEffortRequired |
| native | justifications:DisproportionateEffortRequired |
| exact | dpv_justifications:DisproportionateEffortRequired, dpv_justifications_owl:DisproportionateEffortRequired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DisproportionateEffortRequired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#DisproportionateEffortRequired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it requires a disproportionate effort'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Disproportionate Effort Required
exact_mappings:
- dpv_justifications:DisproportionateEffortRequired
- dpv_justifications_owl:DisproportionateEffortRequired
is_a: NonFulfilmentJustification
class_uri: justifications:DisproportionateEffortRequired

```
</details>

### Induced

<details>
```yaml
name: DisproportionateEffortRequired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#DisproportionateEffortRequired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it requires a disproportionate effort'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Disproportionate Effort Required
exact_mappings:
- dpv_justifications:DisproportionateEffortRequired
- dpv_justifications_owl:DisproportionateEffortRequired
is_a: NonFulfilmentJustification
class_uri: justifications:DisproportionateEffortRequired

```
</details></div>