---
search:
  boost: 10.0
---

# Class: CrimePenaltyExecutionImpaired 


_Justification that the process could not be fulfilled or was not_

_successful because it would interfere with the execution of criminal_

_penalties_



<div data-search-exclude markdown="1">



URI: [justifications:CrimePenaltyExecutionImpaired](https://w3id.org/lmodel/dpv/justifications/CrimePenaltyExecutionImpaired)





```mermaid
 classDiagram
    class CrimePenaltyExecutionImpaired
    click CrimePenaltyExecutionImpaired href "../CrimePenaltyExecutionImpaired/"
      SecurityImpaired <|-- CrimePenaltyExecutionImpaired
        click SecurityImpaired href "../SecurityImpaired/"
      LegalProcessImpaired <|-- CrimePenaltyExecutionImpaired
        click LegalProcessImpaired href "../LegalProcessImpaired/"
      
      
```





## Inheritance
* [NonFulfilmentJustification](NonFulfilmentJustification.md)
    * [LegalProcessImpaired](LegalProcessImpaired.md)
        * **CrimePenaltyExecutionImpaired** [ [SecurityImpaired](SecurityImpaired.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [justifications:CrimePenaltyExecutionImpaired](https://w3id.org/lmodel/dpv/justifications/CrimePenaltyExecutionImpaired) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [JustificationsSubset](JustificationsSubset.md)



## Aliases


* Crime Penalty Execution Impaired




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/justifications/owl#CrimePenaltyExecutionImpaired |
| dpv_extension_slug | justifications |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/justifications




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | justifications:CrimePenaltyExecutionImpaired |
| native | justifications:CrimePenaltyExecutionImpaired |
| exact | dpv_justifications:CrimePenaltyExecutionImpaired, dpv_justifications_owl:CrimePenaltyExecutionImpaired |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CrimePenaltyExecutionImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#CrimePenaltyExecutionImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the execution of criminal

  penalties'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Crime Penalty Execution Impaired
exact_mappings:
- dpv_justifications:CrimePenaltyExecutionImpaired
- dpv_justifications_owl:CrimePenaltyExecutionImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:CrimePenaltyExecutionImpaired

```
</details>

### Induced

<details>
```yaml
name: CrimePenaltyExecutionImpaired
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/justifications/owl#CrimePenaltyExecutionImpaired
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: justifications
description: 'Justification that the process could not be fulfilled or was not

  successful because it would interfere with the execution of criminal

  penalties'
in_subset:
- justifications_subset
from_schema: https://w3id.org/lmodel/dpv/justifications
aliases:
- Crime Penalty Execution Impaired
exact_mappings:
- dpv_justifications:CrimePenaltyExecutionImpaired
- dpv_justifications_owl:CrimePenaltyExecutionImpaired
is_a: LegalProcessImpaired
mixins:
- SecurityImpaired
class_uri: justifications:CrimePenaltyExecutionImpaired

```
</details></div>