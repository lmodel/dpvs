---
search:
  boost: 10.0
---

# Class: ContractPerformanceNecessity 


_Justification that the process could not be fulfilled or was not_

_successful because it is necessary for the performance of a contract_



<div data-search-exclude markdown="1">



URI: [justifications:ContractPerformanceNecessity](https://w3id.org/lmodel/dpv/justifications/ContractPerformanceNecessity)





```mermaid
 classDiagram
    class ContractPerformanceNecessity
    click ContractPerformanceNecessity href "../ContractPerformanceNecessity/"
      LegalProcessImpaired <|-- ContractPerformanceNecessity
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **ContractPerformanceNecessity**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:ContractPerformanceNecessity](https://w3id.org/lmodel/dpv/justifications/ContractPerformanceNecessity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Contract Performance Necessity




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#ContractPerformanceNecessity |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:ContractPerformanceNecessity |
| native | justifications:ContractPerformanceNecessity |
| exact | dpv_justifications:ContractPerformanceNecessity, dpv_justifications_owl:ContractPerformanceNecessity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ContractPerformanceNecessity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ContractPerformanceNecessity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it is necessary for the performance of a contract'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Contract Performance Necessity
exact_mappings:
- dpv_justifications:ContractPerformanceNecessity
- dpv_justifications_owl:ContractPerformanceNecessity
is_a: LegalProcessImpaired
class_uri: justifications:ContractPerformanceNecessity

```
</details>

### Induced

<details>
```yaml
name: ContractPerformanceNecessity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#ContractPerformanceNecessity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it is necessary for the performance of a contract'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Contract Performance Necessity
exact_mappings:
- dpv_justifications:ContractPerformanceNecessity
- dpv_justifications_owl:ContractPerformanceNecessity
is_a: LegalProcessImpaired
class_uri: justifications:ContractPerformanceNecessity

```
</details></div>