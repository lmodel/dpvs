---
search:
  boost: 10.0
---

# Class: EntityAlreadyInformed 


_Justification that the process could not be fulfilled or was not_

_successful because the entity already has the information_



<div data-search-exclude markdown="1">



URI: [justifications:EntityAlreadyInformed](https://w3id.org/lmodel/dpv/justifications/EntityAlreadyInformed)





```mermaid
 classDiagram
    class EntityAlreadyInformed
    click EntityAlreadyInformed href "../EntityAlreadyInformed/"
      DisproportionateEffortRequired <|-- EntityAlreadyInformed
        click DisproportionateEffortRequired href "../DisproportionateEffortRequired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [DisproportionateEffortRequired](DisproportionateEffortRequired.md)
        * **EntityAlreadyInformed**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:EntityAlreadyInformed](https://w3id.org/lmodel/dpv/justifications/EntityAlreadyInformed) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Entity Already Informed




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#EntityAlreadyInformed |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:EntityAlreadyInformed |
| native | justifications:EntityAlreadyInformed |
| exact | dpv_justifications:EntityAlreadyInformed, dpv_justifications_owl:EntityAlreadyInformed |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EntityAlreadyInformed
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#EntityAlreadyInformed
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because the entity already has the information'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Entity Already Informed
exact_mappings:
- dpv_justifications:EntityAlreadyInformed
- dpv_justifications_owl:EntityAlreadyInformed
is_a: DisproportionateEffortRequired
class_uri: justifications:EntityAlreadyInformed

```
</details>

### Induced

<details>
```yaml
name: EntityAlreadyInformed
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#EntityAlreadyInformed
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because the entity already has the information'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Entity Already Informed
exact_mappings:
- dpv_justifications:EntityAlreadyInformed
- dpv_justifications_owl:EntityAlreadyInformed
is_a: DisproportionateEffortRequired
class_uri: justifications:EntityAlreadyInformed

```
</details></div>