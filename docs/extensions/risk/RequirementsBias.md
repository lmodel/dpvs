---
search:
  boost: 10.0
---

# Class: RequirementsBias 


_Bias that occurs in or during requirements creation_



<div data-search-exclude markdown="1">



URI: [risk:RequirementsBias](https://w3id.org/lmodel/dpv/risk/RequirementsBias)





```mermaid
 classDiagram
    class RequirementsBias
    click RequirementsBias href "../RequirementsBias/"
      PotentialConsequence <|-- RequirementsBias
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- RequirementsBias
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- RequirementsBias
        click PotentialRiskSource href "../PotentialRiskSource/"
      CognitiveBias <|-- RequirementsBias
        click CognitiveBias href "../CognitiveBias/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Bias](Bias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [CognitiveBias](CognitiveBias.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **RequirementsBias** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:RequirementsBias](https://w3id.org/lmodel/dpv/risk/RequirementsBias) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Requirements Bias


## Comments

* Requirements bias also represents occasions for the human cognitive
biases to manifest



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 24027:2021 |
| upstream_iri | https://w3id.org/dpv/risk/owl#RequirementsBias |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:RequirementsBias |
| native | risk:RequirementsBias |
| exact | dpv_risk:RequirementsBias, dpv_risk_owl:RequirementsBias |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RequirementsBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RequirementsBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Bias that occurs in or during requirements creation
comments:
- 'Requirements bias also represents occasions for the human cognitive

  biases to manifest'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Requirements Bias
exact_mappings:
- dpv_risk:RequirementsBias
- dpv_risk_owl:RequirementsBias
is_a: CognitiveBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:RequirementsBias

```
</details>

### Induced

<details>
```yaml
name: RequirementsBias
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 24027:2021
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#RequirementsBias
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Bias that occurs in or during requirements creation
comments:
- 'Requirements bias also represents occasions for the human cognitive

  biases to manifest'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Requirements Bias
exact_mappings:
- dpv_risk:RequirementsBias
- dpv_risk_owl:RequirementsBias
is_a: CognitiveBias
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:RequirementsBias

```
</details></div>