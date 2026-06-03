---
search:
  boost: 10.0
---

# Class: MarketUnavailable 


_Status indicating Technology is unavailable on the market_



<div data-search-exclude markdown="1">



URI: [tech:MarketUnavailable](https://w3id.org/lmodel/dpv/tech/MarketUnavailable)





```mermaid
 classDiagram
    class MarketUnavailable
    click MarketUnavailable href "../MarketUnavailable/"
      MarketAvailabilityStatus <|-- MarketUnavailable
        click MarketAvailabilityStatus href "../MarketAvailabilityStatus/"
      
      
```





## Inheritance
* [TechnologyStatus](TechnologyStatus.md)
    * [MarketAvailabilityStatus](MarketAvailabilityStatus.md)
        * **MarketUnavailable**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:MarketUnavailable](https://w3id.org/lmodel/dpv/tech/MarketUnavailable) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Market Unavailable




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#MarketUnavailable |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:MarketUnavailable |
| native | tech:MarketUnavailable |
| exact | dpv_tech:MarketUnavailable, dpv_tech_owl:MarketUnavailable |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MarketUnavailable
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#MarketUnavailable
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status indicating Technology is unavailable on the market
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Market Unavailable
exact_mappings:
- dpv_tech:MarketUnavailable
- dpv_tech_owl:MarketUnavailable
is_a: MarketAvailabilityStatus
class_uri: tech:MarketUnavailable

```
</details>

### Induced

<details>
```yaml
name: MarketUnavailable
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#MarketUnavailable
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status indicating Technology is unavailable on the market
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Market Unavailable
exact_mappings:
- dpv_tech:MarketUnavailable
- dpv_tech_owl:MarketUnavailable
is_a: MarketAvailabilityStatus
class_uri: tech:MarketUnavailable

```
</details></div>