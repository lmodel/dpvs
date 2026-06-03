---
search:
  boost: 10.0
---

# Class: Threat 


_Risk source event which causes Risk_



<div data-search-exclude markdown="1">



URI: [risk:Threat](https://w3id.org/lmodel/dpv/risk/Threat)





```mermaid
 classDiagram
    class Threat
    click Threat href "../Threat/"
      RiskIdentification <|-- Threat
        click RiskIdentification href "../RiskIdentification/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * [RiskAssessment](RiskAssessment.md)
        * [RiskIdentification](RiskIdentification.md)
            * **Threat**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Threat](https://w3id.org/lmodel/dpv/risk/Threat) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Threat




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Threat |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Threat |
| native | risk:Threat |
| exact | dpv_risk:Threat, dpv_risk_owl:Threat |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Threat
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Threat
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risk source event which causes Risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Threat
exact_mappings:
- dpv_risk:Threat
- dpv_risk_owl:Threat
is_a: RiskIdentification
class_uri: risk:Threat

```
</details>

### Induced

<details>
```yaml
name: Threat
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Threat
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risk source event which causes Risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Threat
exact_mappings:
- dpv_risk:Threat
- dpv_risk_owl:Threat
is_a: RiskIdentification
class_uri: risk:Threat

```
</details></div>