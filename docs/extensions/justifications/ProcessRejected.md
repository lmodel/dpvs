---
search:
  boost: 10.0
---

# Class: ProcessRejected 


_Justification that the process could not be fulfilled because of one of_

_more reasons associated with the process itself e.g. it was excessive,_

_malicious, etc._



<div data-search-exclude markdown="1">



URI: [justifications:ProcessRejected](https://w3id.org/lmodel/dpv/justifications/ProcessRejected)





```mermaid
 classDiagram
    class ProcessRejected
    click ProcessRejected href "../ProcessRejected/"
      NonFulfilmentJustification <|-- ProcessRejected
        click NonFulfilmentJustification href "../NonFulfilmentJustification/"
      

      ProcessRejected <|-- ProcessExcessive
        click ProcessExcessive href "../ProcessExcessive/"
      ProcessRejected <|-- ProcessFrivolous
        click ProcessFrivolous href "../ProcessFrivolous/"
      ProcessRejected <|-- ProcessMalicious
        click ProcessMalicious href "../ProcessMalicious/"
      ProcessRejected <|-- ProcessUnfounded
        click ProcessUnfounded href "../ProcessUnfounded/"
      

      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * **ProcessRejected**
        * [ProcessExcessive](ProcessExcessive.md)
        * [ProcessFrivolous](ProcessFrivolous.md)
        * [ProcessMalicious](ProcessMalicious.md)
        * [ProcessUnfounded](ProcessUnfounded.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:ProcessRejected](https://w3id.org/lmodel/dpv/justifications/ProcessRejected) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Process Rejected




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#ProcessRejected |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:ProcessRejected |
| native | justifications:ProcessRejected |
| exact | dpv_justifications:ProcessRejected, dpv_justifications_owl:ProcessRejected |
| related | oscal:RiskAcceptance |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProcessRejected
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ProcessRejected
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled because of one
  of

  more reasons associated with the process itself e.g. it was excessive,

  malicious, etc.'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Process Rejected
exact_mappings:
- dpv_justifications:ProcessRejected
- dpv_justifications_owl:ProcessRejected
related_mappings:
- oscal:RiskAcceptance
is_a: NonFulfilmentJustification
class_uri: justifications:ProcessRejected

```
</details>

### Induced

<details>
```yaml
name: ProcessRejected
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ProcessRejected
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled because of one
  of

  more reasons associated with the process itself e.g. it was excessive,

  malicious, etc.'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Process Rejected
exact_mappings:
- dpv_justifications:ProcessRejected
- dpv_justifications_owl:ProcessRejected
related_mappings:
- oscal:RiskAcceptance
is_a: NonFulfilmentJustification
class_uri: justifications:ProcessRejected

```
</details></div>