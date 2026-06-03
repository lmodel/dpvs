---
search:
  boost: 10.0
---

# Class: RiskCriteria 


_Criteria for determining or evaluating significance of risk_



<div data-search-exclude markdown="1">



URI: [risk:RiskCriteria](https://w3id.org/lmodel/dpv/risk/RiskCriteria)





```mermaid
 classDiagram
    class RiskCriteria
    click RiskCriteria href "../RiskCriteria/"
      RiskManagement <|-- RiskCriteria
        click RiskManagement href "../RiskManagement/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * **RiskCriteria**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RiskCriteria](https://w3id.org/lmodel/dpv/risk/RiskCriteria) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Risk Criteria




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RiskCriteria |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RiskCriteria |
| native | risk:RiskCriteria |
| exact | dpv_risk:RiskCriteria, dpv_risk_owl:RiskCriteria |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskCriteria
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskCriteria
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Criteria for determining or evaluating significance of risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Criteria
exact_mappings:
- dpv_risk:RiskCriteria
- dpv_risk_owl:RiskCriteria
is_a: RiskManagement
class_uri: risk:RiskCriteria

```
</details>

### Induced

<details>
```yaml
name: RiskCriteria
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskCriteria
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Criteria for determining or evaluating significance of risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Criteria
exact_mappings:
- dpv_risk:RiskCriteria
- dpv_risk_owl:RiskCriteria
is_a: RiskManagement
class_uri: risk:RiskCriteria

```
</details></div>