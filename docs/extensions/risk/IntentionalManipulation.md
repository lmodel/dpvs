---
search:
  boost: 10.0
---

# Class: IntentionalManipulation 


_Concept representing Intentional Manipulation_



<div data-search-exclude markdown="1">



URI: [risk:IntentionalManipulation](https://w3id.org/lmodel/dpv/risk/IntentionalManipulation)





```mermaid
 classDiagram
    class IntentionalManipulation
    click IntentionalManipulation href "../IntentionalManipulation/"
      ConfidentialityConcept <|-- IntentionalManipulation
        click ConfidentialityConcept href "../ConfidentialityConcept/"
      IntegrityConcept <|-- IntentionalManipulation
        click IntegrityConcept href "../IntegrityConcept/"
      PotentialConsequence <|-- IntentionalManipulation
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- IntentionalManipulation
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- IntentionalManipulation
        click PotentialRiskSource href "../PotentialRiskSource/"
      MaliciousActivity <|-- IntentionalManipulation
        click MaliciousActivity href "../MaliciousActivity/"
      
      
```





## Inheritance
* [TechnicalRiskConcept](TechnicalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ExternalSecurityThreat](ExternalSecurityThreat.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * [MaliciousActivity](MaliciousActivity.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * **IntentionalManipulation** [ [ConfidentialityConcept](ConfidentialityConcept.md) [IntegrityConcept](IntegrityConcept.md) [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:IntentionalManipulation](https://w3id.org/lmodel/dpv/risk/IntentionalManipulation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Intentional Manipulation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#IntentionalManipulation |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:IntentionalManipulation |
| native | risk:IntentionalManipulation |
| exact | dpv_risk:IntentionalManipulation, dpv_risk_owl:IntentionalManipulation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IntentionalManipulation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IntentionalManipulation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Intentional Manipulation
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Intentional Manipulation
exact_mappings:
- dpv_risk:IntentionalManipulation
- dpv_risk_owl:IntentionalManipulation
is_a: MaliciousActivity
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:IntentionalManipulation

```
</details>

### Induced

<details>
```yaml
name: IntentionalManipulation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#IntentionalManipulation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Intentional Manipulation
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Intentional Manipulation
exact_mappings:
- dpv_risk:IntentionalManipulation
- dpv_risk_owl:IntentionalManipulation
is_a: MaliciousActivity
mixins:
- ConfidentialityConcept
- IntegrityConcept
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:IntentionalManipulation

```
</details></div>