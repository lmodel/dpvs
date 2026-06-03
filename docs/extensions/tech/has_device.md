---
search:
  boost: 5.0
---

# Slot: has_device 


_Indicates the technology has or uses the associated device_



<div data-search-exclude markdown="1">



URI: [tech:has_device](https://w3id.org/lmodel/dpv/tech/has_device)

## Inheritance

* [has_hardware](has_hardware.md)
    * **has_device**








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


* has device




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasDevice |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_device |
| native | tech:has_device |
| exact | dpv_tech:hasDevice, dpv_tech_owl:hasDevice |




## LinkML Source

<details>
```yaml
name: has_device
definition_uri: tech:hasDevice
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasDevice
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the technology has or uses the associated device
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has device
exact_mappings:
- dpv_tech:hasDevice
- dpv_tech_owl:hasDevice
rank: 1000
is_a: has_hardware
range: string
multivalued: true

```
</details></div>