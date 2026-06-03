---
search:
  boost: 10.0
---

# Class: GroupAttributionBias 


_Bias that occurs when a human assumes that what is true for an_

_individual or object is also true for everyone, or all objects, in that_

_group_



<div data-search-exclude markdown="1">



URI: [risk:GroupAttributionBias](https://w3id.org/lmodel/dpv/risk/GroupAttributionBias)





```mermaid
 classDiagram
    class GroupAttributionBias
    click GroupAttributionBias href "../GroupAttributionBias/"
      PotentialConsequence <|-- GroupAttributionBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- GroupAttributionBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- GroupAttributionBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      CognitiveBias <|-- GroupAttributionBias
        click CognitiveBias href "../CognitiveBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [CognitiveBias](CognitiveBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **GroupAttributionBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:GroupAttributionBias](https://w3id.org/lmodel/dpv/risk/GroupAttributionBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Group Attribution Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#GroupAttributionBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:GroupAttributionBias |
| native | risk:GroupAttributionBias |
| exact | dpv_risk:GroupAttributionBias, dpv_risk_owl:GroupAttributionBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GroupAttributionBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#GroupAttributionBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when a human assumes that what is true for an

  individual or object is also true for everyone, or all objects, in that

  group'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Group Attribution Bias
exact_mappings:
- dpv_risk:GroupAttributionBias
- dpv_risk_owl:GroupAttributionBias
is_a: CognitiveBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:GroupAttributionBias

```
</details>

### Induced

<details>
```yaml
name: GroupAttributionBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#GroupAttributionBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when a human assumes that what is true for an

  individual or object is also true for everyone, or all objects, in that

  group'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Group Attribution Bias
exact_mappings:
- dpv_risk:GroupAttributionBias
- dpv_risk_owl:GroupAttributionBias
is_a: CognitiveBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:GroupAttributionBias

```
</details></div>