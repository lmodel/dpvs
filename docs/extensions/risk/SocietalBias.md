---
search:
  boost: 10.0
---

# Class: SocietalBias 


_Bias that occurs when similar cognitive bias (conscious or unconscious)_

_is being held by many individuals in society_



<div data-search-exclude markdown="1">



URI: [risk:SocietalBias](https://w3id.org/lmodel/dpv/risk/SocietalBias)





```mermaid
 classDiagram
    class SocietalBias
    click SocietalBias href "../SocietalBias/"
      PotentialConsequence <|-- SocietalBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- SocietalBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- SocietalBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      CognitiveBias <|-- SocietalBias
        click CognitiveBias href "../CognitiveBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [CognitiveBias](CognitiveBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **SocietalBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:SocietalBias](https://w3id.org/lmodel/dpv/risk/SocietalBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Societal Bias




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#SocietalBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:SocietalBias |
| native | risk:SocietalBias |
| exact | dpv_risk:SocietalBias, dpv_risk_owl:SocietalBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SocietalBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SocietalBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when similar cognitive bias (conscious or unconscious)

  is being held by many individuals in society'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Societal Bias
exact_mappings:
- dpv_risk:SocietalBias
- dpv_risk_owl:SocietalBias
is_a: CognitiveBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SocietalBias

```
</details>

### Induced

<details>
```yaml
name: SocietalBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#SocietalBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Bias that occurs when similar cognitive bias (conscious or unconscious)

  is being held by many individuals in society'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Societal Bias
exact_mappings:
- dpv_risk:SocietalBias
- dpv_risk_owl:SocietalBias
is_a: CognitiveBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:SocietalBias

```
</details></div>