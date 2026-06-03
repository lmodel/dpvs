---
search:
  boost: 10.0
---

# Class: Floods 


_The occurrence or potential occurrence of floods_



<div data-search-exclude markdown="1">



URI: [risk:Floods](https://w3id.org/lmodel/dpv/risk/Floods)





```mermaid
 classDiagram
    class Floods
    click Floods href "../Floods/"
      PotentialConsequence <|-- Floods
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Floods
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Floods
        click PotentialRisk href "../PotentialRisk/"
      EnvironmentalRisk <|-- Floods
        click EnvironmentalRisk href "../EnvironmentalRisk/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [EnvironmentalRisk](EnvironmentalRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **Floods** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Floods](https://w3id.org/lmodel/dpv/risk/Floods) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Floods




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Floods |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Floods |
| native | risk:Floods |
| exact | dpv_risk:Floods, dpv_risk_owl:Floods |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Floods
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Floods
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: The occurrence or potential occurrence of floods
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Floods
exact_mappings:
- dpv_risk:Floods
- dpv_risk_owl:Floods
is_a: EnvironmentalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Floods

```
</details>

### Induced

<details>
```yaml
name: Floods
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Floods
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: The occurrence or potential occurrence of floods
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Floods
exact_mappings:
- dpv_risk:Floods
- dpv_risk_owl:Floods
is_a: EnvironmentalRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Floods

```
</details></div>