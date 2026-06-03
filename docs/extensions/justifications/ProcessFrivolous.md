---
search:
  boost: 10.0
---

# Class: ProcessFrivolous 


_Justification that the process could not be fulfilled or was not_

_successful because it was found to be based on frivolous reasons_



<div data-search-exclude markdown="1">



URI: [justifications:ProcessFrivolous](https://w3id.org/lmodel/dpv/justifications/ProcessFrivolous)





```mermaid
 classDiagram
    class ProcessFrivolous
    click ProcessFrivolous href "../ProcessFrivolous/"
      ProcessRejected <|-- ProcessFrivolous
        click ProcessRejected href "../ProcessRejected/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [ProcessRejected](ProcessRejected.md)
        * **ProcessFrivolous**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:ProcessFrivolous](https://w3id.org/lmodel/dpv/justifications/ProcessFrivolous) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Process Frivolous




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#ProcessFrivolous |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:ProcessFrivolous |
| native | justifications:ProcessFrivolous |
| exact | dpv_justifications:ProcessFrivolous, dpv_justifications_owl:ProcessFrivolous |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProcessFrivolous
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ProcessFrivolous
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it was found to be based on frivolous reasons'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Process Frivolous
exact_mappings:
- dpv_justifications:ProcessFrivolous
- dpv_justifications_owl:ProcessFrivolous
is_a: ProcessRejected
class_uri: justifications:ProcessFrivolous

```
</details>

### Induced

<details>
```yaml
name: ProcessFrivolous
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ProcessFrivolous
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it was found to be based on frivolous reasons'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Process Frivolous
exact_mappings:
- dpv_justifications:ProcessFrivolous
- dpv_justifications_owl:ProcessFrivolous
is_a: ProcessRejected
class_uri: justifications:ProcessFrivolous

```
</details></div>