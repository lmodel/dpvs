---
search:
  boost: 10.0
---

# Class: PhysicalHealth 


_Concept representing physical health of individual(s), or group(s), or_

_society at large_



<div data-search-exclude markdown="1">



URI: [risk:PhysicalHealth](https://w3id.org/lmodel/dpv/risk/PhysicalHealth)





```mermaid
 classDiagram
    class PhysicalHealth
    click PhysicalHealth href "../PhysicalHealth/"
      PotentialConsequence <|-- PhysicalHealth
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- PhysicalHealth
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- PhysicalHealth
        click PotentialRisk href "../PotentialRisk/"
      Health <|-- PhysicalHealth
        click Health href "../Health/"
      

      PhysicalHealth <|-- PhysicalHarm
        click PhysicalHarm href "../PhysicalHarm/"
      

      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * [HealthSafety](HealthSafety.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
            * [Health](Health.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
                * **PhysicalHealth** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PhysicalHealth](https://w3id.org/lmodel/dpv/risk/PhysicalHealth) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Physical Health




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PhysicalHealth |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PhysicalHealth |
| native | risk:PhysicalHealth |
| exact | dpv_risk:PhysicalHealth, dpv_risk_owl:PhysicalHealth |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PhysicalHealth
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PhysicalHealth
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing physical health of individual(s), or group(s),
  or

  society at large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Physical Health
exact_mappings:
- dpv_risk:PhysicalHealth
- dpv_risk_owl:PhysicalHealth
is_a: Health
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PhysicalHealth

```
</details>

### Induced

<details>
```yaml
name: PhysicalHealth
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PhysicalHealth
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing physical health of individual(s), or group(s),
  or

  society at large'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Physical Health
exact_mappings:
- dpv_risk:PhysicalHealth
- dpv_risk_owl:PhysicalHealth
is_a: Health
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:PhysicalHealth

```
</details></div>