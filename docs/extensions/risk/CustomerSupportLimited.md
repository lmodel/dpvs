---
search:
  boost: 10.0
---

# Class: CustomerSupportLimited 


_Concept representing customer support to be limited_



<div data-search-exclude markdown="1">



URI: [risk:CustomerSupportLimited](https://w3id.org/lmodel/dpv/risk/CustomerSupportLimited)





```mermaid
 classDiagram
    class CustomerSupportLimited
    click CustomerSupportLimited href "../CustomerSupportLimited/"
      PotentialConsequence <|-- CustomerSupportLimited
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- CustomerSupportLimited
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- CustomerSupportLimited
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- CustomerSupportLimited
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **CustomerSupportLimited** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:CustomerSupportLimited](https://w3id.org/lmodel/dpv/risk/CustomerSupportLimited) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Customer Support Limited




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#CustomerSupportLimited |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:CustomerSupportLimited |
| native | risk:CustomerSupportLimited |
| exact | dpv_risk:CustomerSupportLimited, dpv_risk_owl:CustomerSupportLimited |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CustomerSupportLimited
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CustomerSupportLimited
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing customer support to be limited
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Customer Support Limited
exact_mappings:
- dpv_risk:CustomerSupportLimited
- dpv_risk_owl:CustomerSupportLimited
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:CustomerSupportLimited

```
</details>

### Induced

<details>
```yaml
name: CustomerSupportLimited
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#CustomerSupportLimited
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing customer support to be limited
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Customer Support Limited
exact_mappings:
- dpv_risk:CustomerSupportLimited
- dpv_risk_owl:CustomerSupportLimited
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:CustomerSupportLimited

```
</details></div>