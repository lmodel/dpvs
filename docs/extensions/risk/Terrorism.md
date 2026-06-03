---
search:
  boost: 10.0
---

# Class: Terrorism 


_Concept representing Terrorism_



<div data-search-exclude markdown="1">



URI: [risk:Terrorism](https://w3id.org/lmodel/dpv/risk/Terrorism)





```mermaid
 classDiagram
    class Terrorism
    click Terrorism href "../Terrorism/"
      PotentialConsequence <|-- Terrorism
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Terrorism
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Terrorism
        click PotentialRisk href "../PotentialRisk/"
      GroupRisk <|-- Terrorism
        click GroupRisk href "../GroupRisk/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [GroupRisk](GroupRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **Terrorism** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Terrorism](https://w3id.org/lmodel/dpv/risk/Terrorism) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Terrorism




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Terrorism |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Terrorism |
| native | risk:Terrorism |
| exact | dpv_risk:Terrorism, dpv_risk_owl:Terrorism |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Terrorism
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Terrorism
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Terrorism
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Terrorism
exact_mappings:
- dpv_risk:Terrorism
- dpv_risk_owl:Terrorism
is_a: GroupRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Terrorism

```
</details>

### Induced

<details>
```yaml
name: Terrorism
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Terrorism
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Terrorism
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Terrorism
exact_mappings:
- dpv_risk:Terrorism
- dpv_risk_owl:Terrorism
is_a: GroupRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Terrorism

```
</details></div>