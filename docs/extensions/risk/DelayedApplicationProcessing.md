---
search:
  boost: 10.0
---

# Class: DelayedApplicationProcessing 


_Concept representing delayed processing of applications_



<div data-search-exclude markdown="1">



URI: [risk:DelayedApplicationProcessing](https://w3id.org/lmodel/dpv/risk/DelayedApplicationProcessing)





```mermaid
 classDiagram
    class DelayedApplicationProcessing
    click DelayedApplicationProcessing href "../DelayedApplicationProcessing/"
      PotentialConsequence <|-- DelayedApplicationProcessing
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- DelayedApplicationProcessing
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- DelayedApplicationProcessing
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- DelayedApplicationProcessing
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **DelayedApplicationProcessing** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:DelayedApplicationProcessing](https://w3id.org/lmodel/dpv/risk/DelayedApplicationProcessing) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Delayed Application Processing




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#DelayedApplicationProcessing |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:DelayedApplicationProcessing |
| native | risk:DelayedApplicationProcessing |
| exact | dpv_risk:DelayedApplicationProcessing, dpv_risk_owl:DelayedApplicationProcessing |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DelayedApplicationProcessing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DelayedApplicationProcessing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing delayed processing of applications
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Delayed Application Processing
exact_mappings:
- dpv_risk:DelayedApplicationProcessing
- dpv_risk_owl:DelayedApplicationProcessing
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:DelayedApplicationProcessing

```
</details>

### Induced

<details>
```yaml
name: DelayedApplicationProcessing
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#DelayedApplicationProcessing
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing delayed processing of applications
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Delayed Application Processing
exact_mappings:
- dpv_risk:DelayedApplicationProcessing
- dpv_risk_owl:DelayedApplicationProcessing
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:DelayedApplicationProcessing

```
</details></div>