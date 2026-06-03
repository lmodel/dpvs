---
search:
  boost: 5.0
---

# Slot: has_market_availability_status 


_Indicates whether the technology is available on the market_



<div data-search-exclude markdown="1">



URI: [tech:has_market_availability_status](https://w3id.org/lmodel/dpv/tech/has_market_availability_status)
<!-- no inheritance hierarchy -->







## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |






## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* has market availability status




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasMarketAvailabilityStatus |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_market_availability_status |
| native | tech:has_market_availability_status |
| exact | dpv_tech:hasMarketAvailabilityStatus, dpv_tech_owl:hasMarketAvailabilityStatus |




## LinkML Source

<details>
```yaml
name: has_market_availability_status
definition_uri: tech:hasMarketAvailabilityStatus
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasMarketAvailabilityStatus
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates whether the technology is available on the market
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has market availability status
exact_mappings:
- dpv_tech:hasMarketAvailabilityStatus
- dpv_tech_owl:hasMarketAvailabilityStatus
rank: 1000
range: string
multivalued: true

```
</details></div>