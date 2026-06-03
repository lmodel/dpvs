---
search:
  boost: 10.0
---

# Class: RM5x5S2L4 


_Node in a 5x5 Risk Matrix with Risk Severity: Low; Likelihood: High; and_

_Risk Level: Moderate_



<div data-search-exclude markdown="1">



URI: [risk:RM5x5S2L4](https://w3id.org/lmodel/dpv/risk/RM5x5S2L4)





```mermaid
 classDiagram
    class RM5x5S2L4
    click RM5x5S2L4 href "../RM5x5S2L4/"
      RiskAnalysis <|-- RM5x5S2L4
        click RiskAnalysis href "../RiskAnalysis/"
      RiskMatrix5x5 <|-- RM5x5S2L4
        click RiskMatrix5x5 href "../RiskMatrix5x5/"
      
      
```





## Inheritance
* [RiskManagement](RiskManagement.md)
    * [RiskAssessment](RiskAssessment.md)
        * [RiskAnalysis](RiskAnalysis.md)
            * [RiskMatrix](RiskMatrix.md)
                * [RiskMatrix5x5](RiskMatrix5x5.md) [ [RiskAnalysis](RiskAnalysis.md)]
                    * **RM5x5S2L4** [ [RiskAnalysis](RiskAnalysis.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RM5x5S2L4](https://w3id.org/lmodel/dpv/risk/RM5x5S2L4) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Moderate Risk (RM5x5 S:2 L:4)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#RM5x5S2L4 |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RM5x5S2L4 |
| native | risk:RM5x5S2L4 |
| exact | dpv_risk:RM5x5S2L4, dpv_risk_owl:RM5x5S2L4 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RM5x5S2L4
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RM5x5S2L4
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Node in a 5x5 Risk Matrix with Risk Severity: Low; Likelihood: High;
  and

  Risk Level: Moderate'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Moderate Risk (RM5x5 S:2 L:4)
exact_mappings:
- dpv_risk:RM5x5S2L4
- dpv_risk_owl:RM5x5S2L4
is_a: RiskMatrix5x5
mixins:
- RiskAnalysis
class_uri: risk:RM5x5S2L4

```
</details>

### Induced

<details>
```yaml
name: RM5x5S2L4
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RM5x5S2L4
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Node in a 5x5 Risk Matrix with Risk Severity: Low; Likelihood: High;
  and

  Risk Level: Moderate'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Moderate Risk (RM5x5 S:2 L:4)
exact_mappings:
- dpv_risk:RM5x5S2L4
- dpv_risk_owl:RM5x5S2L4
is_a: RiskMatrix5x5
mixins:
- RiskAnalysis
class_uri: risk:RM5x5S2L4

```
</details></div>