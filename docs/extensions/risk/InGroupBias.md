---
search:
  boost: 10.0
---

# Class: InGroupBias 


_Bias that occurs when showing partiality to one's own group or own_

_characteristics_



<div data-search-exclude markdown="1">



URI: [risk:InGroupBias](https://w3id.org/lmodel/dpv/risk/InGroupBias)





```mermaid
 classDiagram
    class InGroupBias
    click InGroupBias href "../InGroupBias/"
      PotentialConsequence <|-- InGroupBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- InGroupBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- InGroupBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      CognitiveBias <|-- InGroupBias
        click CognitiveBias href "../CognitiveBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [CognitiveBias](CognitiveBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **InGroupBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:InGroupBias](https://w3id.org/lmodel/dpv/risk/InGroupBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* In-Group Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#InGroupBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:InGroupBias |
| native | risk:InGroupBias |
| exact | dpv_risk:InGroupBias, dpv_risk_owl:InGroupBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InGroupBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InGroupBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when showing partiality to one''s own group or own

  characteristics'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- In-Group Bias
exact_mappings:
- dpv_risk:InGroupBias
- dpv_risk_owl:InGroupBias
is_a: CognitiveBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:InGroupBias

```
</details>

### Induced

<details>
```yaml
name: InGroupBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InGroupBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when showing partiality to one''s own group or own

  characteristics'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- In-Group Bias
exact_mappings:
- dpv_risk:InGroupBias
- dpv_risk_owl:InGroupBias
is_a: CognitiveBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:InGroupBias

```
</details></div>