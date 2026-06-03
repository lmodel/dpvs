---
search:
  boost: 5.0
---

# Slot: has_hardware 


_Indicates the technology has or uses the associated hardware_



<div data-search-exclude markdown="1">



URI: [tech:has_hardware](https://w3id.org/lmodel/dpv/tech/has_hardware)

## Inheritance

* **has_hardware**
    * [has_device](has_device.md)








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


* has hardware




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#hasHardware |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:has_hardware |
| native | tech:has_hardware |
| exact | dpv_tech:hasHardware, dpv_tech_owl:hasHardware |




## LinkML Source

<details>
```yaml
name: has_hardware
definition_uri: tech:hasHardware
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#hasHardware
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Indicates the technology has or uses the associated hardware
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- has hardware
exact_mappings:
- dpv_tech:hasHardware
- dpv_tech_owl:hasHardware
rank: 1000
range: string
multivalued: true

```
</details></div>