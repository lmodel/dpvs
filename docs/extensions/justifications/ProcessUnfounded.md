---
search:
  boost: 10.0
---

# Class: ProcessUnfounded 


_Justification that the process could not be fulfilled or was not_

_successful because it was found to be based on manifestly unfounded_

_reasons_



<div data-search-exclude markdown="1">



URI: [justifications:ProcessUnfounded](https://w3id.org/lmodel/dpv/justifications/ProcessUnfounded)





```mermaid
 classDiagram
    class ProcessUnfounded
    click ProcessUnfounded href "../ProcessUnfounded/"
      ProcessRejected <|-- ProcessUnfounded
        click ProcessRejected href "../ProcessRejected/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [ProcessRejected](ProcessRejected.md)
        * **ProcessUnfounded**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:ProcessUnfounded](https://w3id.org/lmodel/dpv/justifications/ProcessUnfounded) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Process Unfounded




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#ProcessUnfounded |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:ProcessUnfounded |
| native | justifications:ProcessUnfounded |
| exact | dpv_justifications:ProcessUnfounded, dpv_justifications_owl:ProcessUnfounded |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProcessUnfounded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ProcessUnfounded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it was found to be based on manifestly unfounded

  reasons'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Process Unfounded
exact_mappings:
- dpv_justifications:ProcessUnfounded
- dpv_justifications_owl:ProcessUnfounded
is_a: ProcessRejected
class_uri: justifications:ProcessUnfounded

```
</details>

### Induced

<details>
```yaml
name: ProcessUnfounded
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ProcessUnfounded
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it was found to be based on manifestly unfounded

  reasons'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Process Unfounded
exact_mappings:
- dpv_justifications:ProcessUnfounded
- dpv_justifications_owl:ProcessUnfounded
is_a: ProcessRejected
class_uri: justifications:ProcessUnfounded

```
</details></div>