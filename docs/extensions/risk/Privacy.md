---
search:
  boost: 10.0
---

# Class: Privacy 


_Concept representing privacy of humans at an individual, group, or_

_larger societal levels_



<div data-search-exclude markdown="1">



URI: [risk:Privacy](https://w3id.org/lmodel/dpv/risk/Privacy)





```mermaid
 classDiagram
    class Privacy
    click Privacy href "../Privacy/"
      PotentialConsequence <|-- Privacy
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Privacy
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Privacy
        click PotentialRisk href "../PotentialRisk/"
      IndividualRisk <|-- Privacy
        click IndividualRisk href "../IndividualRisk/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [IndividualRisk](IndividualRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **Privacy** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Privacy](https://w3id.org/lmodel/dpv/risk/Privacy) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Privacy




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Privacy |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Privacy |
| native | risk:Privacy |
| exact | dpv_risk:Privacy, dpv_risk_owl:Privacy |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Privacy
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Privacy
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing privacy of humans at an individual, group, or

  larger societal levels'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Privacy
exact_mappings:
- dpv_risk:Privacy
- dpv_risk_owl:Privacy
is_a: IndividualRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Privacy

```
</details>

### Induced

<details>
```yaml
name: Privacy
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Privacy
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing privacy of humans at an individual, group, or

  larger societal levels'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Privacy
exact_mappings:
- dpv_risk:Privacy
- dpv_risk_owl:Privacy
is_a: IndividualRisk
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Privacy

```
</details></div>