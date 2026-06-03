---
search:
  boost: 10.0
---

# Class: RiskPerception 


_Perception or view on risk_



<div data-search-exclude markdown="1">



URI: [risk:RiskPerception](https://w3id.org/lmodel/dpv/risk/RiskPerception)





```mermaid
 classDiagram
    class RiskPerception
    click RiskPerception href "../RiskPerception/"
      RiskManagement <|-- RiskPerception
        click RiskManagement href "../RiskManagement/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * **RiskPerception**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RiskPerception](https://w3id.org/lmodel/dpv/risk/RiskPerception) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Risk Perception




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RiskPerception |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RiskPerception |
| native | risk:RiskPerception |
| exact | dpv_risk:RiskPerception, dpv_risk_owl:RiskPerception |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskPerception
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskPerception
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Perception or view on risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Perception
exact_mappings:
- dpv_risk:RiskPerception
- dpv_risk_owl:RiskPerception
is_a: RiskManagement
class_uri: risk:RiskPerception

```
</details>

### Induced

<details>
```yaml
name: RiskPerception
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskPerception
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Perception or view on risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Perception
exact_mappings:
- dpv_risk:RiskPerception
- dpv_risk_owl:RiskPerception
is_a: RiskManagement
class_uri: risk:RiskPerception

```
</details></div>