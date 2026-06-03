---
search:
  boost: 10.0
---

# Class: ImpactControl 


_Risk Mitigation Measure that controls Impacts_



<div data-search-exclude markdown="1">



URI: [risk:ImpactControl](https://w3id.org/lmodel/dpv/risk/ImpactControl)





```mermaid
 classDiagram
    class ImpactControl
    click ImpactControl href "../ImpactControl/"
      RiskControl <|-- ImpactControl
        click RiskControl href "../RiskControl/"
      

      ImpactControl <|-- AvoidImpact
        click AvoidImpact href "../AvoidImpact/"
      ImpactControl <|-- ChangeImpact
        click ChangeImpact href "../ChangeImpact/"
      ImpactControl <|-- HaltImpact
        click HaltImpact href "../HaltImpact/"
      ImpactControl <|-- RemoveImpact
        click RemoveImpact href "../RemoveImpact/"
      

      
```





## Inheritance
* [RiskControl](RiskControl.md)
    * **ImpactControl**
        * [ChangeImpact](ChangeImpact.md) [ [RiskControl](RiskControl.md) [SubstitutionControl](SubstitutionControl.md)]
        * [HaltImpact](HaltImpact.md) [ [RiskControl](RiskControl.md) [InterruptionControl](InterruptionControl.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ImpactControl](https://w3id.org/lmodel/dpv/risk/ImpactControl) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Impact Control




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ImpactControl |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ImpactControl |
| native | risk:ImpactControl |
| exact | dpv_risk:ImpactControl, dpv_risk_owl:ImpactControl |
| close | iso42001:AIReferenceControl |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ImpactControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ImpactControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risk Mitigation Measure that controls Impacts
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Impact Control
exact_mappings:
- dpv_risk:ImpactControl
- dpv_risk_owl:ImpactControl
close_mappings:
- iso42001:AIReferenceControl
is_a: RiskControl
class_uri: risk:ImpactControl

```
</details>

### Induced

<details>
```yaml
name: ImpactControl
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ImpactControl
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Risk Mitigation Measure that controls Impacts
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Impact Control
exact_mappings:
- dpv_risk:ImpactControl
- dpv_risk_owl:ImpactControl
close_mappings:
- iso42001:AIReferenceControl
is_a: RiskControl
class_uri: risk:ImpactControl

```
</details></div>