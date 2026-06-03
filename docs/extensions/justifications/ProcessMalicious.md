---
search:
  boost: 10.0
---

# Class: ProcessMalicious 


_Justification that the process could not be fulfilled or was not_

_successful because it was found to be malicious e.g. with intent to_

_cause disruption or harassment_



<div data-search-exclude markdown="1">



URI: [justifications:ProcessMalicious](https://w3id.org/lmodel/dpv/justifications/ProcessMalicious)





```mermaid
 classDiagram
    class ProcessMalicious
    click ProcessMalicious href "../ProcessMalicious/"
      ProcessRejected <|-- ProcessMalicious
        click ProcessRejected href "../ProcessRejected/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [ProcessRejected](ProcessRejected.md)
        * **ProcessMalicious**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:ProcessMalicious](https://w3id.org/lmodel/dpv/justifications/ProcessMalicious) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Process Malicious




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#ProcessMalicious |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:ProcessMalicious |
| native | justifications:ProcessMalicious |
| exact | dpv_justifications:ProcessMalicious, dpv_justifications_owl:ProcessMalicious |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProcessMalicious
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ProcessMalicious
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it was found to be malicious e.g. with intent to

  cause disruption or harassment'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Process Malicious
exact_mappings:
- dpv_justifications:ProcessMalicious
- dpv_justifications_owl:ProcessMalicious
is_a: ProcessRejected
class_uri: justifications:ProcessMalicious

```
</details>

### Induced

<details>
```yaml
name: ProcessMalicious
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ProcessMalicious
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it was found to be malicious e.g. with intent to

  cause disruption or harassment'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Process Malicious
exact_mappings:
- dpv_justifications:ProcessMalicious
- dpv_justifications_owl:ProcessMalicious
is_a: ProcessRejected
class_uri: justifications:ProcessMalicious

```
</details></div>