---
search:
  boost: 10.0
---

# Class: RiskOwner 


_Entity accountable for managing risk_



<div data-search-exclude markdown="1">



URI: [risk:RiskOwner](https://w3id.org/lmodel/dpv/risk/RiskOwner)





```mermaid
 classDiagram
    class RiskOwner
    click RiskOwner href "../RiskOwner/"
      RiskManagement <|-- RiskOwner
        click RiskManagement href "../RiskManagement/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * **RiskOwner**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RiskOwner](https://w3id.org/lmodel/dpv/risk/RiskOwner) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Risk Owner




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RiskOwner |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RiskOwner |
| native | risk:RiskOwner |
| exact | dpv_risk:RiskOwner, dpv_risk_owl:RiskOwner |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RiskOwner
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskOwner
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Entity accountable for managing risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Owner
exact_mappings:
- dpv_risk:RiskOwner
- dpv_risk_owl:RiskOwner
is_a: RiskManagement
class_uri: risk:RiskOwner

```
</details>

### Induced

<details>
```yaml
name: RiskOwner
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RiskOwner
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Entity accountable for managing risk
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Risk Owner
exact_mappings:
- dpv_risk:RiskOwner
- dpv_risk_owl:RiskOwner
is_a: RiskManagement
class_uri: risk:RiskOwner

```
</details></div>