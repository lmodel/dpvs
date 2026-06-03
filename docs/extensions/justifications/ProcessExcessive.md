---
search:
  boost: 10.0
---

# Class: ProcessExcessive 


_Justification that the process could not be fulfilled or was not_

_successful because it was found to be excessive in nature_



<div data-search-exclude markdown="1">



URI: [justifications:ProcessExcessive](https://w3id.org/lmodel/dpv/justifications/ProcessExcessive)





```mermaid
 classDiagram
    class ProcessExcessive
    click ProcessExcessive href "../ProcessExcessive/"
      ProcessRejected <|-- ProcessExcessive
        click ProcessRejected href "../ProcessRejected/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [ProcessRejected](ProcessRejected.md)
        * **ProcessExcessive**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:ProcessExcessive](https://w3id.org/lmodel/dpv/justifications/ProcessExcessive) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Process Excessive




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#ProcessExcessive |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:ProcessExcessive |
| native | justifications:ProcessExcessive |
| exact | dpv_justifications:ProcessExcessive, dpv_justifications_owl:ProcessExcessive |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProcessExcessive
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ProcessExcessive
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it was found to be excessive in nature'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Process Excessive
exact_mappings:
- dpv_justifications:ProcessExcessive
- dpv_justifications_owl:ProcessExcessive
is_a: ProcessRejected
class_uri: justifications:ProcessExcessive

```
</details>

### Induced

<details>
```yaml
name: ProcessExcessive
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ProcessExcessive
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it was found to be excessive in nature'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Process Excessive
exact_mappings:
- dpv_justifications:ProcessExcessive
- dpv_justifications_owl:ProcessExcessive
is_a: ProcessRejected
class_uri: justifications:ProcessExcessive

```
</details></div>