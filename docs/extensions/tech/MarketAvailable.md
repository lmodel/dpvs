---
search:
  boost: 10.0
---

# Class: MarketAvailable 


_Status indicating Technology is available on the market_



<div data-search-exclude markdown="1">



URI: [tech:MarketAvailable](https://w3id.org/lmodel/dpv/tech/MarketAvailable)





```mermaid
 classDiagram
    class MarketAvailable
    click MarketAvailable href "../MarketAvailable/"
      MarketAvailabilityStatus <|-- MarketAvailable
        click MarketAvailabilityStatus href "../MarketAvailabilityStatus/"
      
      
```





## Inheritance
* [TechnologyStatus](TechnologyStatus.md)
    * [MarketAvailabilityStatus](MarketAvailabilityStatus.md)
        * **MarketAvailable**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:MarketAvailable](https://w3id.org/lmodel/dpv/tech/MarketAvailable) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Market Available




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#MarketAvailable |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:MarketAvailable |
| native | tech:MarketAvailable |
| exact | dpv_tech:MarketAvailable, dpv_tech_owl:MarketAvailable |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MarketAvailable
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#MarketAvailable
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status indicating Technology is available on the market
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Market Available
exact_mappings:
- dpv_tech:MarketAvailable
- dpv_tech_owl:MarketAvailable
is_a: MarketAvailabilityStatus
class_uri: tech:MarketAvailable

```
</details>

### Induced

<details>
```yaml
name: MarketAvailable
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#MarketAvailable
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status indicating Technology is available on the market
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Market Available
exact_mappings:
- dpv_tech:MarketAvailable
- dpv_tech_owl:MarketAvailable
is_a: MarketAvailabilityStatus
class_uri: tech:MarketAvailable

```
</details></div>