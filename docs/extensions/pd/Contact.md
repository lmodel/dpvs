---
search:
  boost: 10.0
---

# Class: Contact 


_Information about contacts or used for contacting e.g. email address or_

_phone number_



<div data-search-exclude markdown="1">



URI: [pd:Contact](https://w3id.org/lmodel/dpv/pd/Contact)





```mermaid
 classDiagram
    class Contact
    click Contact href "../Contact/"
      Tracking <|-- Contact
        click Tracking href "../Tracking/"
      

      Contact <|-- EmailAddress
        click EmailAddress href "../EmailAddress/"
      Contact <|-- PhysicalAddress
        click PhysicalAddress href "../PhysicalAddress/"
      Contact <|-- TelephoneNumber
        click TelephoneNumber href "../TelephoneNumber/"
      

      
```





## Inheritance
* [Tracking](Tracking.md)
    * **Contact**
        * [EmailAddress](EmailAddress.md)
        * [PhysicalAddress](PhysicalAddress.md) [ [DpvLocation](DpvLocation.md)]
        * [TelephoneNumber](TelephoneNumber.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Contact](https://w3id.org/lmodel/dpv/pd/Contact) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Contact




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Contact |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Contact |
| native | pd:Contact |
| exact | dpv_pd:Contact, dpv_pd_owl:Contact |
| related | svd:Physical |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Contact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Contact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about contacts or used for contacting e.g. email address
  or

  phone number'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Contact
exact_mappings:
- dpv_pd:Contact
- dpv_pd_owl:Contact
related_mappings:
- svd:Physical
is_a: Tracking
class_uri: pd:Contact

```
</details>

### Induced

<details>
```yaml
name: Contact
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Contact
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about contacts or used for contacting e.g. email address
  or

  phone number'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Contact
exact_mappings:
- dpv_pd:Contact
- dpv_pd_owl:Contact
related_mappings:
- svd:Physical
is_a: Tracking
class_uri: pd:Contact

```
</details></div>