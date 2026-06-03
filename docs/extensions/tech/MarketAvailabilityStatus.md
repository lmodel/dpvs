---
search:
  boost: 10.0
---

# Class: MarketAvailabilityStatus 


_Status indicating whether Technology is available on the market_



<div data-search-exclude markdown="1">



URI: [tech:MarketAvailabilityStatus](https://w3id.org/lmodel/dpv/tech/MarketAvailabilityStatus)





```mermaid
 classDiagram
    class MarketAvailabilityStatus
    click MarketAvailabilityStatus href "../MarketAvailabilityStatus/"
      TechnologyStatus <|-- MarketAvailabilityStatus
        click TechnologyStatus href "../TechnologyStatus/"
      

      MarketAvailabilityStatus <|-- MarketAvailable
        click MarketAvailable href "../MarketAvailable/"
      MarketAvailabilityStatus <|-- MarketUnavailable
        click MarketUnavailable href "../MarketUnavailable/"
      

      
```





## Inheritance
* [TechnologyStatus](TechnologyStatus.md)
    * **MarketAvailabilityStatus**
        * [MarketAvailable](MarketAvailable.md)
        * [MarketUnavailable](MarketUnavailable.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:MarketAvailabilityStatus](https://w3id.org/lmodel/dpv/tech/MarketAvailabilityStatus) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Market Availability Status




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#MarketAvailabilityStatus |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:MarketAvailabilityStatus |
| native | tech:MarketAvailabilityStatus |
| exact | dpv_tech:MarketAvailabilityStatus, dpv_tech_owl:MarketAvailabilityStatus |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MarketAvailabilityStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#MarketAvailabilityStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status indicating whether Technology is available on the market
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Market Availability Status
exact_mappings:
- dpv_tech:MarketAvailabilityStatus
- dpv_tech_owl:MarketAvailabilityStatus
is_a: TechnologyStatus
class_uri: tech:MarketAvailabilityStatus

```
</details>

### Induced

<details>
```yaml
name: MarketAvailabilityStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#MarketAvailabilityStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Status indicating whether Technology is available on the market
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Market Availability Status
exact_mappings:
- dpv_tech:MarketAvailabilityStatus
- dpv_tech_owl:MarketAvailabilityStatus
is_a: TechnologyStatus
class_uri: tech:MarketAvailabilityStatus

```
</details></div>