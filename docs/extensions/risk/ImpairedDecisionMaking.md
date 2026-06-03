---
search:
  boost: 10.0
---

# Class: ImpairedDecisionMaking 


_Concept representing Impaired Decision Making_



<div data-search-exclude markdown="1">



URI: [risk:ImpairedDecisionMaking](https://w3id.org/lmodel/dpv/risk/ImpairedDecisionMaking)





```mermaid
 classDiagram
    class ImpairedDecisionMaking
    click ImpairedDecisionMaking href "../ImpairedDecisionMaking/"
      PotentialConsequence <|-- ImpairedDecisionMaking
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ImpairedDecisionMaking
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ImpairedDecisionMaking
        click PotentialRisk href "../PotentialRisk/"
      IndividualRisk <|-- ImpairedDecisionMaking
        click IndividualRisk href "../IndividualRisk/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ImpairedDecisionMaking** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ImpairedDecisionMaking](https://w3id.org/lmodel/dpv/risk/ImpairedDecisionMaking) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Impaired Decision Making




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ImpairedDecisionMaking |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ImpairedDecisionMaking |
| native | risk:ImpairedDecisionMaking |
| exact | dpv_risk:ImpairedDecisionMaking, dpv_risk_owl:ImpairedDecisionMaking |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ImpairedDecisionMaking
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ImpairedDecisionMaking
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Impaired Decision Making
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Impaired Decision Making
exact_mappings:
- dpv_risk:ImpairedDecisionMaking
- dpv_risk_owl:ImpairedDecisionMaking
is_a: IndividualRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ImpairedDecisionMaking

```
</details>

### Induced

<details>
```yaml
name: ImpairedDecisionMaking
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ImpairedDecisionMaking
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Impaired Decision Making
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Impaired Decision Making
exact_mappings:
- dpv_risk:ImpairedDecisionMaking
- dpv_risk_owl:ImpairedDecisionMaking
is_a: IndividualRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ImpairedDecisionMaking

```
</details></div>