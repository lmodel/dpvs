---
search:
  boost: 10.0
---

# Class: DisabilityDiscrimination 


_Discrimination against individuals based on physical or mental_

_disabilities_



<div data-search-exclude markdown="1">



URI: [risk:DisabilityDiscrimination](https://w3id.org/lmodel/dpv/risk/DisabilityDiscrimination)





```mermaid
 classDiagram
    class DisabilityDiscrimination
    click DisabilityDiscrimination href "../DisabilityDiscrimination/"
      PotentialConsequence <|-- DisabilityDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- DisabilityDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- DisabilityDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- DisabilityDiscrimination
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **DisabilityDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DisabilityDiscrimination](https://w3id.org/lmodel/dpv/risk/DisabilityDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Disability Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DisabilityDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DisabilityDiscrimination |
| native | risk:DisabilityDiscrimination |
| exact | dpv_risk:DisabilityDiscrimination, dpv_risk_owl:DisabilityDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DisabilityDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DisabilityDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination against individuals based on physical or mental

  disabilities'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Disability Discrimination
exact_mappings:
- dpv_risk:DisabilityDiscrimination
- dpv_risk_owl:DisabilityDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:DisabilityDiscrimination

```
</details>

### Induced

<details>
```yaml
name: DisabilityDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DisabilityDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Discrimination against individuals based on physical or mental

  disabilities'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Disability Discrimination
exact_mappings:
- dpv_risk:DisabilityDiscrimination
- dpv_risk_owl:DisabilityDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:DisabilityDiscrimination

```
</details></div>