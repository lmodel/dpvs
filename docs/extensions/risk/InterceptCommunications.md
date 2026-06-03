---
search:
  boost: 10.0
---

# Class: InterceptCommunications 


_Concept representing Interception of Communications_



<div data-search-exclude markdown="1">



URI: [risk:InterceptCommunications](https://w3id.org/lmodel/dpv/risk/InterceptCommunications)





```mermaid
 classDiagram
    class InterceptCommunications
    click InterceptCommunications href "../InterceptCommunications/"
      ConfidentialityConcept <|-- InterceptCommunications
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      PotentialConsequence <|-- InterceptCommunications
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- InterceptCommunications
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- InterceptCommunications
        click PotentialRiskSource href "../PotentialRiskSource/"
      MaliciousActivity <|-- InterceptCommunications
        click MaliciousActivity href "../MaliciousActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [MaliciousActivity](MaliciousActivity.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **InterceptCommunications** [ [ConfidentialityConcept](ConfidentialityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:InterceptCommunications](https://w3id.org/lmodel/dpv/risk/InterceptCommunications) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Intercept Communications


## Comments

* This concept was called "InterceptionCommunications" in DPV 2.0



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#InterceptCommunications |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:InterceptCommunications |
| native | risk:InterceptCommunications |
| exact | dpv_risk:InterceptCommunications, dpv_risk_owl:InterceptCommunications |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InterceptCommunications
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InterceptCommunications
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Interception of Communications
comments:
- This concept was called "InterceptionCommunications" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Intercept Communications
exact_mappings:
- dpv_risk:InterceptCommunications
- dpv_risk_owl:InterceptCommunications
is_a: MaliciousActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:InterceptCommunications

```
</details>

### Induced

<details>
```yaml
name: InterceptCommunications
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#InterceptCommunications
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Interception of Communications
comments:
- This concept was called "InterceptionCommunications" in DPV 2.0
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Intercept Communications
exact_mappings:
- dpv_risk:InterceptCommunications
- dpv_risk_owl:InterceptCommunications
is_a: MaliciousActivity
mixins:
- ConfidentialityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:InterceptCommunications

```
</details></div>