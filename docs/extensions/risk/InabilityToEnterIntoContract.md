---
search:
  boost: 10.0
---

# Class: InabilityToEnterIntoContract 


_Concept representing inability to enter into contract_



<div data-search-exclude markdown="1">



URI: [risk:InabilityToEnterIntoContract](https://w3id.org/lmodel/dpv/risk/InabilityToEnterIntoContract)





```mermaid
 classDiagram
    class InabilityToEnterIntoContract
    click InabilityToEnterIntoContract href "../InabilityToEnterIntoContract/"
      PotentialConsequence <|-- InabilityToEnterIntoContract
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- InabilityToEnterIntoContract
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- InabilityToEnterIntoContract
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- InabilityToEnterIntoContract
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **InabilityToEnterIntoContract** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:InabilityToEnterIntoContract](https://w3id.org/lmodel/dpv/risk/InabilityToEnterIntoContract) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Inability to Enter Into Contract




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#InabilityToEnterIntoContract |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:InabilityToEnterIntoContract |
| native | risk:InabilityToEnterIntoContract |
| exact | dpv_risk:InabilityToEnterIntoContract, dpv_risk_owl:InabilityToEnterIntoContract |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InabilityToEnterIntoContract
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InabilityToEnterIntoContract
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing inability to enter into contract
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Inability to Enter Into Contract
exact_mappings:
- dpv_risk:InabilityToEnterIntoContract
- dpv_risk_owl:InabilityToEnterIntoContract
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:InabilityToEnterIntoContract

```
</details>

### Induced

<details>
```yaml
name: InabilityToEnterIntoContract
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InabilityToEnterIntoContract
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing inability to enter into contract
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Inability to Enter Into Contract
exact_mappings:
- dpv_risk:InabilityToEnterIntoContract
- dpv_risk_owl:InabilityToEnterIntoContract
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:InabilityToEnterIntoContract

```
</details></div>