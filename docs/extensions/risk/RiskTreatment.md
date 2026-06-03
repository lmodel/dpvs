---
search:
  boost: 10.0
---

# Class: RiskTreatment 


_Process by which risk is modified and mitigated_



<div data-search-exclude markdown="1">



URI: [risk:RiskTreatment](https://w3id.org/lmodel/dpv/risk/RiskTreatment)





```mermaid
 classDiagram
    class RiskTreatment
    click RiskTreatment href "../RiskTreatment/"
      RiskManagement <|-- RiskTreatment
        click RiskManagement href "../RiskManagement/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * **RiskTreatment**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RiskTreatment](https://w3id.org/lmodel/dpv/risk/RiskTreatment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Risk Treatment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RiskTreatment |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RiskTreatment |
| native | risk:RiskTreatment |
| exact | dpv_risk:RiskTreatment, dpv_risk_owl:RiskTreatment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskTreatment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskTreatment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Process by which risk is modified and mitigated
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Treatment
exact_mappings:
- dpv_risk:RiskTreatment
- dpv_risk_owl:RiskTreatment
is_a: RiskManagement
class_uri: risk:RiskTreatment

```
</details>

### Induced

<details>
```yaml
name: RiskTreatment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskTreatment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Process by which risk is modified and mitigated
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Treatment
exact_mappings:
- dpv_risk:RiskTreatment
- dpv_risk_owl:RiskTreatment
is_a: RiskManagement
class_uri: risk:RiskTreatment

```
</details></div>